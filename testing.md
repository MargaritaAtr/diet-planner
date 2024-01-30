

# Testing documentation for Diet Planner website.
<br>

![Alt text](/docs/readme/images/pancakes.png)

# Contents

* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JS Validation](#js-validation)
    * [CI Python Linter](#ci-python-linter)
    * [Lighthouse](#lighthouse)
* [User Story Testing](#user-story-testing)
    * [General](#general)
    * [Logged Out](#logged-out)
    * [User Logged In](#user-logged-in)
* [Manual Testing](#manual-testing)
* [Responsiveness](#responsiveness)
* [Fixed Bugs](#fixed-bugs)

<br><br>

# Validation

## HTML Validation

 The label attribute was missing in option element in all forms for meal categories. Once this has been corrected , all pages pass HTML Validation with some minor warnings to use h2-h6 elements.

![Alt text](/docs/validation-images/errors-edit-meal.png)

<details>
<summary>Homepage</summary>
<br>

![Alt text](/docs/validation-images/homepage.png)
</details>

<details>
<summary>Recipes</summary>
<br>

![Alt text](/docs/validation-images/recipes.png)
</details>
<details>
<summary>Planned meals</summary>
<br>

![Alt text](/docs/validation-images/planned-meals.png)
</details>
</details>
<details>
<summary>Add recipe</summary>
<br>

![Alt text](/docs/validation-images/add-recipe.png)
</details>
<details>
<summary>Edit recipe</summary>
<br>

![Alt text](/docs/validation-images/edit-recipe.png)
</details>


<details>
<summary>Edit meal</summary>
<br>

![Alt text](/docs/validation-images/edit-meal.png.png)
</details>

<details>
<summary>Register</summary>
<br>
There was a closing tag for div missing.

![Alt text](/docs/validation-images/register-error.png)

![Alt text](/docs/validation-images/register.png)
</details>

<details>
<summary>404 page</summary>
<br>

![Alt text](/docs/validation-images/404.png)
</details>

## CSS Validation

CSS file pass CSS Validation at [W3C CSS validation service](https://jigsaw.w3.org/css-validator/) with no errors or warnings.


![Alt text](/docs/validation-images/css-validation.png)

## JS Validation

The Diet planner website passed test using the JSHint Validator tool.

![Alt text](/docs/validation-images/js-validation.png)

## CI Python Linter

![Alt text](/docs/validation-images/python-validator.png)

The Python file successfully passed through the CI PEP8 linter without any warnings, except for a single instance where a line exceeded the recommended length. I addressed this by breaking the line into two, ensuring compliance with PEP8 standards.

## Lighthouse

<details>
<summary>Homepage</summary>
<br>

![Alt text](/docs/lighthouse-images/homepage.png)
</details>

<details>
<summary>Recipes</summary>
<br>

![Alt text](/docs/lighthouse-images/recipes.png)
</details>
<details>
<summary>Planned meals</summary>
<br>

![Alt text](/docs/lighthouse-images/planned-meals.png)
</details>
</details>
<details>
<summary>Edit recipe</summary>
<br>

![Alt text](/docs/lighthouse-images/edit-recipe.png)
</details>


<details>
<summary>Edit meal</summary>
<br>

![Alt text](/docs/lighthouse-images/edit-meal.png)
</details>

<details>
<summary>Register</summary>
<br>

![Alt text](/docs/lighthouse-images/register.png)
</details>

<details>
<summary>Log In page</summary>
<br>

![Alt text](/docs/lighthouse-images/login.png)
</details>

<details>
<summary>404 error page</summary>
<br>

![Alt text](/docs/lighthouse-images/error.png)
</details>

# User Story Testing

## General

| User Story                                                                                | Feature                                                                                                                                    |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| I want to immediately identify the purpose of the site.                                   | Logo displaying app name and background images of homepage.                                                |
| I want navigation to be simple and intuitive.                                             | The navigation links follow established design norms, utilizing a right-aligned layout and a universally recognized hamburger icon for mobile devices. The displayed links vary depending on whether the user is logged in or not. |
| I aim to access the website seamlessly on any device.                                        | The website achieves full responsiveness through the utilization of the Materialize framework's grid system.                                                               |
| I want to be able to easily navigate to the homepage incase of broken link or site error. | Error pages such as 404 and 500 are presented for instances of invalid links or server errors.                                                                      |
<br><br>

## Logged Out 

| User Story                                        | Feature                                                                    |
| ------------------------------------------------- | -------------------------------------------------------------------------- |
| I want to be able to login/register to the service. | Both login and registration functionalities are accessible, either through a call-to-action on the homepage or in the navigation bar. |
| I want to be able to view recipe page , where recipes presented on cards. |The recipe page is open to the public for viewing, but only registered users have the privilege to add, edit, or delete recipes. |

<br><br>

## User Logged In

| User Story                                        | Feature                                                                    |
| ------------------------------------------------- | -------------------------------------------------------------------------- |
| I want to be able to view recipe page with all recipes and  available features for users. | Functions such as adding, editing, and deleting recipes are exclusive to registered users.|
| I would like to view a meal schedule that already includes planned meals and be able to edit/delete them. | All meals displayed in table with edit and delete buttons. Edit button re-directs to edit form.|
 | I want to be able add new recipe. | "Add new recipe" button displayed on recipe page and directs users to the corresponding form for adding a new recipe.|
 | I want to be able to edit existing recipe.| "Edit " button displayed on recipe card and re-directs to the corresponding form for editing a recipe.|
 |I want to be able to add meal to meal schedule, specifying a date, meal category and recipes available on the website. | The "Plan my meal" option is visibly featured in the navbar and redirects to the corresponding meal planning form.|
| I want the ability to mark a meal as urgent if shopping is required.  | The "Tickle" option is provided on the meal planning form for this purpose.|
| I would like to have the option to cancel actions such as deleting, adding, or editing from the respective forms.| The back and cancel buttons present in all forms and re-direct to previous page.|


<br><br>

## Manual Testing

| Feature/Test                                          | Expected Outcome.                                                                                                        | Result |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------ |
| Nav Links.                                            | Redirect to relevant pages.                                                                                              | Pass.  |
| Side Nav                                              | Navbar collapes to Sidenav on mobile devices with correct links.                                                         | Pass.  |
| Login button on Homepage.                         | Redirects to login page.                                                                                                 | Pass.  |
| Login Form - empty.                                   | Will not submit if empty fields.                                                                                         | Pass.  |
| Login Form - incorrect username.                      | Form submits but doesn't login, Flash message comes up " Incorrect Username and/or Password"                                                  | Pass.  |
| Login Form - incorrect password.                      | Form submits but doesn't login, Flash message comes up " Incorrect Username and/or Password"reason.                                                   | Pass.  |
| Login Form - correct details.                         | Form submits and redirects user Recipes page with Flash message "Welcome, (user name)                                                         | Pass.  |
| Register link on Log In Form.                         | Redirects to register page.                                                                                              | Pass.  |
| Register Form - empty.                                | Will not submit if empty fields.                                                                                         | Pass.  |
| Register Form - username exists.                      | Form submits but does not register user, Flash message comes up " Username already exists, try another name."                                 | Pass.  |
| Register Form - new user details.                     | Form submits adding new user and redirects to Homepage with Flash message "Registration Successful!                             | Pass.  |
| Log In link on Register Form                          | Redirects to Log In page.                                                                                                | Pass.  |
| Log Out Button.                                       | Logs user out, clears session cookies and redirects to Homepage.                                                         | Pass.  |
| Add New Recipe Button.                                       | Redirects to Add new recipe page with empty form.                                                         | Pass.  |
| Meal Category selection on recipe form.                                      | Select one option of meal categories.                                                         | Pass.  |
|Submit add recipe - empty form.                                     | Form does not submit. Recipe name/meal category/ingredients/instructions are required.                                                     | Pass.  |
|Add recipe form - completed .                                   | Form submits, once press "Submit" button and save recipe in recipes page. Redirect to all recipes pages.                                                    | Pass.  |
|Back button on add recipe form.                                   | Redirects to all recipes in case the user changed mind to add a new recipe.                                                  | Pass.  |
|Plus sign on recipe card.                                   | Card expands and dispalys Recipe name/Ingredients/Instructions/Calories/Cooking time and Edit button.                                                 | Pass.  |
|Delete button on recipe card.                            | Modal pops up prompting user to confirm if he wants to delete or cancel                               | Pass.  | 
|Delete on modal.                            | Deletes recipe meal from database/website.                            | Pass.  |
|Edit button on recipe card.                                   | Redirects to Edit recipe page with selected recipe details.                                                 | Pass.  |
|Cancel button on edit recipe form .                                 | Redirects to Edit recipe page to all recipe page.                                                 | Pass.  |
|Edit button on edit recipe form.                                  | Updates recipe and redirect to recipe page with Flash message " Recipe successfully edited"                                                | Pass.  |
|Plan meal form. - empty                              | Will not submit if empty. Due date/ meal category and meal name are required.                                              | Pass.  |
|Due date picker on plan meal form.                            | When click on due date, calendar comes up with option select date, months, year.                                             | Pass.  |
| Meal category on plan meal form.                             | Gives the options meal categories                                           | Pass.  |
| Meal name on plan meal form.                             | Provides all recipes saved in database.                                         | Pass.  |
|Is shopping required tickle.                            | When a user selects a shopping required , an attention sign should appear on the corresponding planned meal line on the Planned Meals page.                                    | Pass.  |                                                                                         
|Plan meal - form completed.                            | Form submints and redirect to all planned meals with Flash message " "Meal Successfully added to your weekly plan"                                   | Pass.  | 
|Edit button on planned meals.                            | Redirects to edit meal page with edit meal form. Form aleady completed with relevant fields of this meal.                                   | Pass.  | 
|Cancel button on edit meal form.                            | Redirects to to all planned meals.                                 | Pass.  | 
|Edit button on edit meal form.                            | Updates the meal accordignly.                                | Pass.  | 
|Delete button on planned meals schedule.                            | Modal pops up prompting user to confirm if he wants to delete or cancel                               | Pass.  | 
|Delete on modal.                            | Deletes planned meal from database/website.                            | Pass.  | 
|Cancel on modal.                            | Cancels action and returns to all planned meals schedule.                           | Pass.  | 
|Type a non-existent page path.                          | Redirects to 404 page.                      | Pass.  | 

## Browser Compatibility

The site was tested in Google Chrome, Microsoft Edge and Mozilla Firefox on desktop.

The site was tested in Safari on mobile and tablet.

No issues arose during browser testing.

## Responsiveness

Responsivity tests were carried out using Google Chrome DevTools. Device screen sizes covered include:

- iPhone SE
- iPhone XR
- iPhone 12 Pro
- Pixel 7
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- iPad Mini
- iPad Air
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Samsung Galaxy A51/71
- Nest Hub
- Nest Hub Max

I also personally tested the website on iPhone 10, iPad Pro 2nd Generation, Dell widescreen monitor. All pages looks good on all screen sizes.

## Fixed Bugs

* It appeared that there was an issue with the "Delete" functionality on the meal/recipe page. The current implementation, utilizing a Modal structure from Materialize.css, presents the confirmation modal when the "Delete" button is clicked. However, upon confirming the deletion, it consistently removed the first recipe/meal on the website, rather than the selected one. After persistent efforts and exploration, I have discovered that a crucial adjustment is needed in the href attribute of the trigger. Specifically, changing from href="{{url_for('delete_recipe', recipe_id=recipe._id)}}" to href="#{{recipe._id}}". Additionally, instead of using id="modal1", utilizing id="{{recipe._id}}" is necessary. This modification is applicable across all meal pages as well.

* During HTML testing, an error was identified indicating that the option element for the meal category cannot be without a label. In response, I have rectified this issue by adding a label to the respective option.