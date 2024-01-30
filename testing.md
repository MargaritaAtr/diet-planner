

# Testing documentation for Diet Planner website.
<br>

# Contents

* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JS Validation](#js-validation)
    * [CI Python Linter](#ci-python-linter)
    * [Lighthouse](#lighthouse)
    * [WAVE Accessibility](#wave-accessibility-checker)
* [User Story Testing](#user-story-testing)
    * [General](#general)
    * [Logged Out](#logged-out)
    * [Member User](#member-user)
* [Manual Testing](#manual-testing)
* [Responsiveness](#responsiveness)

<br><br>

## HTML Validation

All pages pass HTML Validation with some minor warnings


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


## CSS Validation

CSS file pass CSS Validation at [W3C CSS validation service](https://jigsaw.w3.org/css-validator/) with no errors or warnings.


![Alt text](/docs/validation-images/css-validation.png)

## JS Validation

The Diet planner website passed test using the JSHint Validator tool.

![Alt text](/docs/validation-images/js-validation.png)

## CI Python Linter

![Alt text](/docs/validation-images/python-validator.png)

The Python file successfully passed through the CI PEP8 linter without any warnings, except for a single instance where a line exceeded the recommended length. I addressed this by breaking the line into two, ensuring compliance with PEP8 standards.

