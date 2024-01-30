# Diet Planner

This is my Milestone Project 3 submission for Code Institute's Diploma in Web Application Development course. 

Diet Planner is a website where you can plan your meal schedule using recipes available on the database and submit new recipes to the website. The website design is responsive and can be used on any device. 

The website is live and the link can be fund [Here](https://diet-planner-b614f893e50e.herokuapp.com)
<br>


![Alt text](/docs/readme/images/responsive.png)

## `Table of Contents`

## [UX](#ux "UX")
  + [Site Goals](#site-goals "Site Goals")
  + [Visitors Goals](#visitors-goals "Visitor Goals")
  + [Audience](#audience "Audience")
 ## [Design](#design "Design")
  + [Colour scheme](#colourscheme "Colour scheme")
  + [Typography](#typography "Typography")
  + [Imagery](#imagery "Imagery") 
 ## [Features](#features "Features")
 + [Existing Features](#existing-features "Existing Features")
 + [Future Features](#future-features "Future Features")
## [Testing](#testing "Testing")
## [Technologies Used](#technologies-used "Technologies Used")
  + [ Languages Used](#languages-used " Languages Used")
  + [Frameworks, Programs Used](#frameworks-programs-used "Frameworks, Programs Used")
## [Deployment and Local Development](#deployment-and-local-development "Deployment and Local Development")
## [Credits](#credits "Credits")
 
## `UX`

## `Site Goals:` 

The goal of a diet planner website is to provide users with tools and resources to help them plan and manage their dietary habits effectively.

## `Visitors Goals:` 

### As first time user:

+ I want to identify the purpose of the website immediately.
+ I want to be able to see all available recipes.
+ I want to be able to register for account.
+ I want to be able to view a website on any device.

### As existing user:

+ I want to be able to login in to my account.
+ I want to be able to add/edit/delete my own recipes.
+ I want to be able to add meal to meal planner. choosing a date, meal category and recipes available on the website. 
+ I want to be able to see other users' recipes and select them for my meal schedule.
+ I want to be able to delete and edit my meal plan.
+ I want to be able to flag if shopping is required.
+ I want to be able cancel  'recipes' edit form and return to all recipes page.
+ I want to be able cancel  'meal' edit form and return to planned meals page.
+ I want to be able to access and use the website on any device.

### As website owner:

+ I want users to navigate easily from page to page using the navigation bar.
+ I want users to be able to submit, delete, and edit their recipes.
+  I want users to be able to plan their meals, choosing a date, meal category and recipes available on the website. 
+ I want the website to look responsive on any device.

## `Audience:`

The audience for a diet planner can be quite diverse and may include individuals with various health and wellness goals. Here are some potential audience groups for a diet planner: 
+ Individuals Looking to Lose Weight
+ Fitness Enthusiasts
+ Busy Professionals
+ Those with Dietary Restrictions

## `Design`

The website exudes a playful and vibrant ambience. The lively pictures of meals showcased on the homepage beckon non-users to explore the site, enticing them with a visual feast of recipes and encouraging them to register for an account.

## `Colour scheme:`

![Alt text](/docs/readme/images/colors.png)

The chosen primary colors consist of a rich black and brown, complemented by a white background, creating a visually appealing contrast. Vibrant colors such as blue, purple, and green have been strategically employed for buttons, ensuring they are eye-catching and engaging.

<br>

## `Typography:`
 Bacasime has been used for entire body.
The icons used  for social media links are from [Font Awesome.](https://fontawesome.com/)
<br>

## `Imagery:`

The all images for this webisite have been taken from [Unsplash.](https://unsplash.com)

<br>

# `Existing Features`

## Navigation bar


![Alt text](/docs/readme/images/navbar1.png)
<br>

![Alt text](/docs/readme/images/navbar2.png)

* Navigation bar provides various options whether the user is logged in as existing user in or not registered.
* The non-users can see Home , Recipes, Logn In and Register options
* The users can see Home, Recipes, Planned meals, plan my meals and log out options from navigation bar.
* The Logo links to the homepage if you click on it.
* The nav bar turns into a slide-out menu on smaller sizes devices.
<br>

## Homepage

![Alt text](/docs/readme/images/login_button.png)

![Alt text](/docs/readme/images/burger-home.png)

The homepage welcomes all users with a dynamic auto-slider showcasing four images in the background. For unregistered users, a conspicuous "Login" button flashes alongside an encouraging message, prompting them to register. Once a user is logged in, both the message and button seamlessly disappear, providing a tailored and streamlined experience.
<br>

## Register page

![Alt text](/docs/readme/images/register.png)

* The register page include the form with input fileds for Username, First name, Last Name and Password.
* The user password is hashed for security.
* There is large button of Register.
* Also there is link to Log in with accompanying message "Already Registered?"
* Every username must be distinct. Therefore, during the registration process for a new user, the system checks if the entered username already exists. In case of a match, a flash message notifies the user that user already exists and to choose a different username.

![Alt text](/docs/readme/images/username.png)

## Log In page

![Alt text](/docs/readme/images/login.png)

* Logn In page include the form with fields for Username and Password and large button to Log In.
* Also there is link to Register Account with accompanying message " Not Registered yet?"
* If the user enters an incorrect username or password, a flash message will appear to notify them of the error.

![Alt text](/static/readme/images/incorrect-user.png)

 * Once the user logged in, a flash messgae comes up with meaaseg " Welcome (username)" and redirect to planned meals page. 
![Alt text](/static/readme/images/welcome.png)

## Flash Messages

![Alt text](/docs/readme/images/flash-mess1.png)

<br>

![Alt text](/docs/readme/images/flash2.png)

* Flash messages will be displayed to confirm user actions such as logging in or out, adding, editing, or deleting a recipe, as well as adding or removing meal from meal schedule.
* The design of the flash messages aligns with the overall aesthetics of the site. These messages effectively alert the user without being overly distracting, contributing to a positive user experience.

## Recipes page

![Alt text](/docs/readme/images/non-users-recipes.png)
![Alt text](/docs/readme/images/users-recipes.png)

* The Recipes page is accessible to both users and non-users. Non-users have the privilege to view recipes exclusively.
* For registered users, the functionality expands, allowing them to add new recipes, as well as edit and delete their own creations. However, the ability to modify and delete recipes is limited to one's own submissions, while other recipes are available for viewing only.

![Alt text](/docs/readme/images/recipe-cards.png)

* The recipes are presented in slide-up cards, utilizing Materializecss. On the front of each card, there is a default image of sandwiches, the category name, a delete button, and a plus sign. When a user clicks the plus sign, the card expands, revealing the complete recipe details, including the recipe name, ingredients, instructions, cooking time, calories, and an "Edit" button.


## Add New Recipe page

![Alt text](/docs/readme/images/add_newrecipe.png)

* Add new recipe page incoporate page with distinct purple submit button and back button, providing users with the option to navigate back to their Recipes page.

## Input fields include :

- Recipe name ( required- text - max 50 characters)
- Meal Category ( selected from dropdown- required)
- Ingredients ( required - text - comma seperated, max - 500 characters)
- Instructions ( required - tex- comma seperated, no max characters)
- Calories (not required - number)
- Cooking time ( not required - number)
- Image Url (not required ,no max characters )

* Every input undergoes validation and is accompanied by clear labels, ensuring a robust and user-friendly data entry experience.
* The image URL is currently experiencing issues, and, for the time being, a default picture of sandwiches has been designated as a temporary placeholder. 

## Edit Recipe page

![Alt text](/docs/readme/images/edit-recipe.png)

* The edit recipe functionality mirrors the input fields present in the "add new recipe" section. When a user engages with the recipe editing feature, the content effortlessly fills the respective input fields.
* The edit page features an "Edit" button and a red "Cancel" button. In the event that a user changes their mind about editing, they can easily navigate back to the recipes page using the "Cancel" button.

## Delete recipe feature

![Alt text](/docs/readme/images/delete-recipe.png)

* Upon clicking the delete button on a recipe card, a window appears with the message "Are you sure you want to delete this recipe?" accompanied by two options: "Delete" and "Cancel." If the user chooses to delete, the recipe will be removed both from the website and the database. Alternatively, the user can opt to cancel this action.

## Plan my meals ahead page

![Alt text](/docs/readme/images/plan-meals.png)

* The meal planning page allows users to proactively plan their meals by filling out a form.

    The form include input fileds:

- The "Due date" field is required. Upon clicking the field, a calendar interface appears, enabling users to choose a date, cancel the selection, or clear the field. The system is configured to automatically prevent the selection of past dates.

- Meal category (required) - selected from dropdown list.Users can choose a meal category, such as breakfast, lunch, and more.
* Meal name (required)- selected from dropdown list of recipe names available on the website.
* Meal notes, while optional, provide a text field where users can leave additional comments or notes if they wish to do so.
* If a user selects this "is shopping required" option, it will be flagged as urgent on the "Planned Meals" page.
* The form also comprises "Cancel" and "Add Meal" buttons. Opting for the "Add Meal" button will result in the meal being displayed on the meal schedule on the Planned Meals page.

## Planned Meals page

![Alt text](/docs/readme/images/planned-meals.png)

* The "Planned Meals" page showcases a schedule of previously selected meals by the user. 
* The schedule details include the day, date, meal category, and an attention sign indicating urgency, specifically if shopping is required.
* Within each schedule entry, options for delete, edit, and a dropdown cursor are available. Clicking the cursor expands the field, revealing additional information such as meal name, meal notes, and the user's name.
* It's important to note that users can exclusively view their own planned meals, ensuring privacy and personalized access.

## Edit meal page

![Alt text](/docs/readme/images/edit-meal.png)

* The edit meal form mirrors the structure of the add meal form, automatically populating with the fields of the selected meal for editing.
* Within this form, users encounter "Cancel" and "Edit" buttons for managing their edits. 
* Additionally, if the user opts to delete the meal, a confirmation message "Are you sure you want to delete this meal?" prompts a decision.

## 404 error page

![Alt text](/docs/readme/images/404error.png)

* If page is not found , it directs to page with message "404 Page not found" .

# `Future Features`

* I want to incorporate a search button for finding recipes by name.
* I want to introduce filter functionality on the Recipe page, allowing users to filter recipes by meal category, user submissions, or submission date.
* I want to implement user account management features such as the ability to edit or delete an account, as well as a password reset option.

# `Testing`

For testing please the [Testing](/testing.md) documentation.
<br><br>

# `Technologies Used`

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

# Frameworks Libraries and Programs

- [Heroku](https://id.heroku.com/login)
  - I utilized Heroku as the deployment source for this project.

- [MongoDB](https://www.mongodb.com/)
    - I used MongoDB for my non-relational database.

- [Flask](https://flask.palletsprojects.com/en/2.2.x/templating/)
  - Templating language I've used with Python to add logic to my html templates.

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  - Templating language I've used with Python to add logic to my html templates.

- [Materialize CSS](https://materializecss.com/)
  - Front-end library with HTML, CSS and Javascript based componants. I used features including Nav bar, Cards, Buttons, Forms and Modal.

- [jQuery](https://jquery.com/)
  - I used jQuery to add functionality to MaterialiseCSS componants.

- [Google Fonts](https://fonts.google.com/)
  - Bacasime Anitique font imported from google fonts.
  
- [Font awesome](https://fontawesome.com/)
  - I used icons from font awesome on buttons.

- [Git](https://git-scm.com/)
  - Git was used as a version control in the terminal.

- [Github](https://github.com/)
  - Github was used to create and store the project repository.

- [Vscode](https://code.visualstudio.com//)
  - Visual Studio Code was used to create my files and where I wrote the code.

- [Miro](https://miro.com/)
  - Miro was used to create Wireframes for the project during the initial planning stage.

  - [Imageresizer](https://imageresizer.com/)
  - Imagerisizer was used to resize images for a faster loading time.

- [TinyPNG](https://tinypng.com/)
  - TinyPNG was used to compress images for a faster loading time.

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
  - Google Chrome's Dev Tools were used while building the project to test responsiveness and for debugging.

- [Unsplash](https://unsplash.com/)
  - Unsplash was used to get images for the website

# Deployment

## Creating a VScode Workspace

The project was created in VScode using the Code Institute Gitpod Full Template using these steps:

## Making a Local Clone

1. Log in (or sign up) to GitHub.
2. Select the relevant repository.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Visual code editor, select "clone repository" and then paste the link you copied from GitHub into  address bar. Enter.
5. Select the location where you want to save a repository and  press Enter. 

## Forking the GitHub Repository

Forks are used to propose changes to someone else's project or to use someone else's project as a starting point for your own idea. By forking the GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository.

To Fork a Github Repository:

1. Log in to GitHub and go to the 
2. Locate the Fork button in the top-right corner of the page, click Fork.
3. You should now have a copy of the original repository in your GitHub account.


Click [Here](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo) for the GitHub quick start guide with images and more detailed explanations of the above process.

## Creating an application with Heroku

You will need to deploy the application using Heroku.

1. Create a requirements.txt file by typing ``` pip3 freeze --local > requirements.txt ``` into the Gitpod CLI. Ensure this is added to your .gitignore file.
2. Create a Procfile by typing ```echo web: python app.py > Procfile```. Open it and ensure it doesn't have a new line, as this can create errors. Ensure it starts with a capital P.
3. Add and commit these files to Github.
4. Go to [Heroku](https://dashboard.heroku.com/apps). Log in or create an account
5. Click the 'New' button and click 'Create new app'.
6. Enter a unique name for your project with no capital letters or spaces and select your region. Click 'Create App'.
7. Inside your project, go to the Resources tab and create a Heroku Postgres Database
8. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
9. Add in the following variables
  - IP : 0.0.0.0
  - PORT : 5000
  - MONGO_DBNAME : Your MongoDB database name
  - MONGO_URI : This can be found on MongoDB by going to Clusters, Connect, Connect to your application
  - SECRET_KEY : Your secret key
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. To connect your Heroku database, go to 'More' in the top right and select run console. Enter ```python3``` to access the python intepreter.










