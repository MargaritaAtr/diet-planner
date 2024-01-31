import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    """
    Renders the homepage.

    Returns:
        flask.render_template: The rendered HTML template for the homepage.
    """
    return render_template("homepage.html")


@app.route("/all_meals")
def all_meals():
    """
    Retrieves all meals from the MongoDB database and renders the
    'all_meals' template.

    Returns:
        flask.render_template: The rendered HTML template for displaying
        all meals.
    """

    meals = list(mongo.db.meals.find())
    return render_template("all_meals.html", meals=meals)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handles user registration.

    If the request method is POST:
    - Checks if the provided username already exists in the database.
    - If username is unique, creates a new user and inserts the user data
    into the database.
    - Sets the new user into the session cookie.
    - Redirects to the homepage with a flash message indicating
    successful registration.

    If the request method is GET:
    - Renders the 'register' template for user registration.

    Returns:
        For POST request:
            flask.redirect: Redirects to the homepage after
            successful registration.
        For GET request:
            flask.render_template: Renders the HTML template
            for user registration.
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, try another name.")
            return redirect(url_for("register"))

        # create new user
        register = {
            "username": request.form.get("username").lower(),
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home", username=session["user"]))

    # For GET request
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handles user login.

    If the request method is POST:
    - Checks if the provided username exists in the database.
    - If the username exists, verifies if the hashed password
    matches the user input.
    - If the password is correct, sets the user into the session cookie and
    redirects to the 'recipes' page.
    - If the password is incorrect, displays an error flash message
    and redirects to the login page.

    If the request method is GET:
    - Renders the 'login' template for user login.

    Returns:
        For POST request:
            flask.redirect: Redirects to the 'recipes' page
            after successful login.
        For GET request:
            flask.render_template: Renders the HTML template for user login.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
            request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    # For GET request
    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Clears all session cookies and redirects to the homepage.

    Returns:
        flask.redirect: Redirects to  homepage after clearing session cookies.
    """
    # clear all session cookies
    session.clear()
    return redirect(url_for("home"))


@app.route("/plan_meals", methods=["GET", "POST"])
def plan_meals():
    """
    Handles the planning of meals.

    If the request method is POST:
    - Retrieves form data to create a new meal.
    - Inserts the new meal into the database.
    - Displays a flash message indicating successful addition and redirects
    to the 'all_meals' page.

    If the request method is GET:
    - Retrieves category and recipe data from the database.
    - Renders the 'plan_meals' template for planning meals,
    displaying available categories and recipes.

    Returns:
        For POST request:
            flask.redirect: Redirects to the 'all_meals' page after
            successfully adding a new meal.
        For GET request:
            flask.render_template: Renders the HTML template for
            planning meals.
    """
    if request.method == "POST":
        is_shopping_required = "on" if request.form.get(
            "is_shopping_required") else "off"
        meal = {
            "due_date": request.form.get("due_date"),
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name").capitalize(),
            "meal_notes": request.form.get("meal_notes"),
            "is_shopping_required": is_shopping_required,
            "created_by": session["user"]
        }
        mongo.db.meals.insert_one(meal)
        flash("Meal Successfully added to your plan")
        return redirect(url_for("all_meals"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    recipes = mongo.db.recipes.find().sort("recipe_name", 1)
    return render_template("plan_meals.html",
                           categories=categories, recipes=recipes)


@app.route("/edit_meal/<meal_id>", methods=["GET", "POST"])
def edit_meal(meal_id):
    """
    Handles the editing of a specific meal.

    If the request method is POST:
    - Retrieves form data to update the selected meal.
    - Updates the meal in the database.
    - Displays a flash message indicating successful editing and
    redirects to the 'all_meals' page.

    If the request method is GET:
    - Retrieves the meal data from the database based on the provided meal_id.
    - Renders the 'edit_meal' template for editing the selected meal,
    displaying available categories.

    Parameters:
        meal_id (str): The unique identifier of the meal to be edited.

    Returns:
        For POST request:
            flask.redirect: Redirects to the 'all_meals' page after
            successfully editing the meal.
        For GET request:
            flask.render_template: Renders the HTML template
            for editing the meal.

    Raises:
        404 Error: If the specified meal_id does not exist in the database.
    """
    if request.method == "POST":
        is_shopping_required = "on" if request.form.get("is_shopping_required") else "off"
        update = {
            "due_date": request.form.get("due_date"),
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name").capitalize(),
            "meal_notes": request.form.get("meal_notes"),
            "is_shopping_required": is_shopping_required,
            "created_by": session["user"]
        }
        mongo.db.meals.update_one({"_id": ObjectId(meal_id)}, {"$set": update})
        flash("Meal successfully edited.")
        return redirect(url_for("all_meals"))

    meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})

    if meal is None:
        abort(404)
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_meal.html", meal=meal, categories=categories)


@app.route("/delete_meal/<meal_id>")
def delete_meal(meal_id):
    """
    Handles the deletion of a specific meal.

    Parameters:
        meal_id (str): The unique identifier of the meal to be deleted.

    Returns:
        flask.redirect: Redirects to the 'all_meals' page after
        successfully deleting the meal.
    """
    mongo.db.meals.delete_one({"_id": ObjectId(meal_id)})
    flash("Meal Deleted")
    return redirect(url_for("all_meals"))


@app.route("/recipes")
def recipes():
    """
    Renders the 'recipes' template, displaying all available recipes.

    Returns:
        flask.render_template: Renders the HTML template for
        displaying all recipes.
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Handles the addition of a new recipe.

    If the request method is POST:
    - Retrieves form data to create a new recipe.
    - Inserts the new recipe into the database.
    - Displays a flash message indicating successful addition and
    redirects to the 'recipes' page.

    If the request method is GET:
    - Retrieves category data from the database.
    - Renders the 'add_recipe' template for adding a new recipe,
    displaying available categories.

    Returns:
        For POST request:
            flask.redirect: Redirects to the 'recipes' page after
            successfully adding a new recipe.
        For GET request:
            flask.render_template: Renders the HTML template for
            adding a new recipe.
    """
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "image_url": request.form.get("image_url"),
            "instructions": request.form.get("instructions"),
            "ingredients": request.form.get("ingredients"),
            "calories": request.form.get("calories"),
            "cooking_time": request.form.get("cooking_time"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully added!")
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/back")
def back():
    """
    Redirects to the 'recipes' page.

    Returns:
        flask.redirect: Redirects to the 'recipes' page.
    """
    return redirect(url_for("recipes"))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Handles the deletion of a specific recipe.

    Parameters:
        recipe_id (str): The unique identifier of the recipe to be deleted.

    Returns:
        flask.redirect: Redirects to the 'recipes' page after successfully
        deleting the recipe.
    """
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted")
    return redirect(url_for("recipes"))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Handles the editing of a specific recipe.

    If the request method is POST:
    - Retrieves form data to update the selected recipe.
    - Updates the recipe in the database.
    - Displays a flash message indicating successful editing and redirects
    to the 'recipes' page.

    If the request method is GET:
    - Retrieves the recipe data from the database based on the
    provided recipe_id.
    - Renders the 'edit_recipe' template for editing the selected recipe,
    displaying available categories.

    Parameters:
        recipe_id (str): The unique identifier of the recipe to be edited.

    Returns:
        For POST request:
            flask.redirect: Redirects to the 'recipes' page after successfully
            editing the recipe.
        For GET request:
            flask.render_template: Renders the HTML template for editing
            the recipe.

    Raises:
        404 Error: If the specified recipe_id does not exist in the database.
    """
    if request.method == "POST":
        edit_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "image_url": request.form.get("image_url"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "calories": request.form.get("calories"),
            "cooking_time": request.form.get("cooking_time"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
        {"$set": edit_recipe})
        flash("Recipe successfully edited")
        return redirect(url_for("recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if recipe is None:
        abort(404)
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", categories=categories,
    recipe=recipe)


@app.errorhandler(404)
def page_not_found(error):
    """
    Handles the 404 error, page not found.

    Parameters:
        error (Exception): The exception object representing the 404 error.

    Returns:
        flask.render_template: Renders the '404_error' template
        for a page not found.
    """
    return render_template("404_error.html")


@app.errorhandler(500)
def internal_error(error):
    """
    Handles the 500 error, internal server error.

    Parameters:
        error (Exception): The exception object representing the 500 error.

    Returns:
        Tuple[flask.render_template, int]: Returns a tuple containing
        the '500_error' template and
        the HTTP status code 500 for an internal server error.
    """
    return render_template("500_error.html"), 500


if __name__ == "__main__":
    """
    Entry point for running the Flask application.

    Checks if the script is executed directly, and if so:
    - Retrieves the host and port information from the environment
    variables (IP and PORT).
    - Runs the Flask application with debug mode enabled.

    Note: This block is executed only if the script is run directly,
    not when it's imported as a module.

    Returns:
        None
    """
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

