import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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
    return render_template("homepage.html")

@app.route("/all_meals")
def all_meals():
    meals= list(mongo.db.meals.find())
    return render_template("all_meals.html", meals=meals)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # create new user
        register = {
            "username": request.form.get("username").lower(),
            "fname" : request.form.get("fname").lower(),
            "lname" : request.form.get("lname").lower(),
            "password": generate_password_hash(request.form.get("password")),
            
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home", username=session["user"]))
        
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(request.form.get("username")))
                        return redirect(url_for(
                         "all_meals", username=session["user"]))                
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/my_meals/<username>", methods=["GET", "POST"])
def my_meals(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("my_meals.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
     #clear all session cookies
     session.clear()
     return redirect(url_for("home"))


@app.route("/plan_meals", methods=["GET", "POST"])
def plan_meals():
    if request.method == "POST":
        is_shopping_required = "on" if request.form.get("is_shopping_required") else "off"
        meal = {
            "due_date": request.form.get("due_date"),
            "category_name": request.form.get("category_name"),
            "meal_name": request.form.get("meal_name"),
            "meal_description": request.form.get("meal_description"),
            "is_shopping_required": is_shopping_required,
            "created_by": session["user"]
        }
        mongo.db.meals.insert_one(meal)
        flash("Meal Successfully added to your weekly plan")
        return redirect(url_for("all_meals"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("plan_meals.html", categories=categories) 


@app.route("/edit_meal/<meal_id>", methods=["GET","POST"])
def edit_meal(meal_id):
    if request.method == "POST":
        is_shopping_required = "on" if request.form.get("is_shopping_required") else "off"
        update = {
            "due_date": request.form.get("due_date"),
            "category_name": request.form.get("category_name"),
            "meal_name": request.form.get("meal_name"),
            "meal_description": request.form.get("meal_description"),
            "is_shopping_required": is_shopping_required,
            "created_by": session["user"]
        }
        mongo.db.meals.update_one({"_id": ObjectId(meal_id)}, {"$set":update})
        flash("Meal Updated")
        
    meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_meal.html", meal=meal , categories=categories)

@app.route("/delete_meal/<meal_id>")
def delete_meal(meal_id):
    mongo.db.meals.delete_one({"_id": ObjectId(meal_id)})
    flash("Meal Deleted")
    return redirect(url_for("all_meals"))  

@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {   
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "image_url": request.form.get("image_url"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully added")
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories) 

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
