# Testing
[back to README.md file](https://github.com/Gregory4321/ciao-down/blob/master/README.md)

## Table of Contents:
* [Validators](#validators)
    * [W3C Validators](#w3c-validators)
    * [JSHint Validator](#jshint-validator)
    * [PEP8](#pep8)
* [DevTools](#devtools)
* [Site Testing](#site-testing)
    * [Manual Testing](#manual-testing)
    <!-- * [Navigation Bar](#navigation-bar)
    * [Footer](#footer)
    * [Back To Top Button](#back-to-top-button)
    * [Home Page](#home-page)
    * [Categories Page](#categories-page)
    * [Add Recipe Page](#add-recipe-page)
    * [Profile Page](#profile-page)
    * [Edit Recipe Page](#edit-recipe-page)
    * [Recipe Page](#recipe_page)
    * [Search Results Page](#search-results-page) -->

* [User Testing](#user-testing)
    * [Peer Code Review](peer-code-review)
    * [User Review](user-review)
    * [Further Testing](#further-testing)
    * [Bugs Found](#bugs-found)

***

## Validators

Testing this site was conducted using various methods to identify any bugs throughout the site. I tested thoroughly throughout building the site, and when the build was completed. I used automatic testing in the form of W3C Validators, JSHint, and PEP8.

### W3C Validators

The W3C Markup Validator and W3C CSS Validator Services were used to validate the code on all of the pages and to make sure that there were no syntax errors in the project. Both the HTML and CSS code were run through these services regularly during the building of this project to ensure the code was valid throughout the process and to avoid nasty suprises at the end.

* [W3C Markup Validator](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

#### HTML

Throughout the different HTML files, errros were thrown for each page, but none that were not expected with the way this code was executed.

[HTML structure error](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/html-error.png)
* These errors were consistent across all of the html pages, except the base.html. This happened due to all of the templates being an extension of the base template; only the base.html included the doctype, language and head tags, but injected them into the other pages, hence why the validator threw these errors and thought no doctype was declared.

[URL for error](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/url-for-errors.png)
* These errors also occured across all pages. The validator did not expect to find 'url_for' in the palce of an images src, an anchors href or forms action.

[Jinja error](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/jinja-erros.png)
* These errors were expected as the validator didn't know what to make of the Jinja templating language.

All these errors are nothing to worry about as they are not errors that affect the code in any way.
I also made use throughout the build to keep my eye on the problems tab in the console of the Gitpod IDE. Each html page also threw errors about the doctype not being declared, but could be ignored due to the exectution of using the base template to inject the doctype and language into the pther templates. An error was also indicated on the edit_recipe page. This was due to two ID's being present twice. This can also be ignored as only one of the ID's would be used at any given time due to Jinja if statements. An error of 'Special characters must be escaped' showed here too, but again it is inside a jinja for loop.
* [Console errors](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/console-errors.png)


[Unknown error](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/unknown-error.png)
* I am unsure why these errors were prompted from the validator. I checked over the code again and there were no mistakes with the positioning of tags. I even moved the head title tags outside of the head tag, and a linter error was thrown.
    * [Tag Error](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/tag-errors.png)

#### CSS

Passing my script.css file through the it passed with no errors.

[CSS Validation Passed](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/css-validation.png)

### JSHint Validator

* [JSHint](https://jshint.com/)

The JSHint validator was used to pass the JS code through and increase the code quality and detect any potential bugs. It pointed out 'let' was available in ES6 (use 'esversion: 6'). I was able to easily recify this problem by using 'var' instead of 'let'.
It also showed what variables were unused or undefined. The undefined variables was just returning the '$' from the jQuery used from materialize and other code. The unused variables realted to the top button and back button. I believe these warnings can be overlooked as the code works fine. I decided not to make any changes to these errors.

[Unused variable error](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/vars-unused.png)

### PEP8

My python file was passed through the [PEP8](http://pep8online.com/) validator. Is passed with no problems. I believe this was due to the fact that the linter installed on my chosen IDE made me keep my code PEP8 compliant whilst writing the code, by throwing visual linting errors.

[Python Validation Passed](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/python-validation.png)

[Back to Top](#table-of-contents)

***

## DevTools

Google Chrome DevTools was used for rigorous testing of the site, from start to finish. It was used for various different reasons. 

* It tested for the responsiveness of the site across multiple screen resolutions.
* Each time I added a new feature, I was able to identify margin and padding issues, making it easy for me to resolve any issues.
* I discovered that the text overlayed on the slider images worked great on large screens, but on the smaller screen sizes it overflowed off the image at the bottom, making it not completely visible.
* It was also very useful at pinpointing what styling was overriding the cards images. I had trouble getting the images to fit the cards the same, not matter what image was uploaded.
* Deciding what to show and what not to show was made easy too with DevTools. It helped reveal that the profile page accordion needed better styling as the screen resolution decreased.
* I had previously edited the code to control the toggle buttons on the add recipe page, to help space them out and wrap them when the screen hit a certain breakpoint. I was bale to find with DevTools that I had forgot to include the same styling on the edit recipe form.
* The Materialize grid system was updated and implemented more often to control how the columns responded.
* When opening the site the console produced and error regarding the favicon. A link tag was added into the head of the base template which resolved this issue.
* The line height of the home icon in the navbar was higher than the hamburger icon when on mobile screen sizes
    
* Debugging
    * Highlighted incorrect use of styling and/or Materialize.
    * Most of the issues above were addressed using media queires to alter sizes, changing margins and paddings, line heights and font sizes across the various screen sizes.
    * Console.log was used and placed amoungst the code to debug any issues.

***


## Site Testing

### User Stories from User Experience (UX) Section



### Manual Testing

#### Navigation Bar

* Home icon - returns the user to the home/index page
* Logo - also returns the user to the home/index page
* Log In - directs the user to the login page
* Sign Up - direct the user to the register page
* Hamburger icon - activates the side nav
    * Logo - returns the user to the home/index page
    * Categories - activates the dropdown, revealing the categories
        * All - directs the user to the recipes page showing all recipes
        * Starters - directs the user to the recipes page showing just the starter recipes
        * Mains - directs the user to the recipes page showing just the mains recipes
        * Desserts - directs the user to the recipes page showing just the dessert recipes
    * Add Recipe - visible if logged in - directs the user to the add recipe page form
    * Profile - visible if logged in - directs a user to the profile page
    * Logout - visible if logged in - directs a user to the log in page

#### Footer

* Social icons - directs the user to the corresponding social page

#### Back-To-Top Button

* Becomes visible after a user scrolls past 200 pixels of the page - directs the user back to the top of the page

All of these features above are present on all pages of the site.

***

#### Home Page

* Search bar - allows a user to type in a keyword
    * Search button - direct the user to the search results page, populating any data that matches their query, otherwise return a try again message
    * Reset button - reloads the home page and resets the search bar
* Featured recipes cards - 
    * when hovered over, reveals the recipes name
    * when clicked, directs the user to that specific recipes page

#### Categories Page

* Back button - directs the user back to the previous page they were on
* Slider control buttons - allows the user to select with slider image to view, otherwise it changes automatically over time
* Recipe card - directs the user to the recipe page of the recipe card clicked

#### Add Recipe Page

* Back button - directs the user back to the previous page they were on
* Slider control buttons - allows the user to select with slider image to view, otherwise it changes automatically over time
* Add recipe form - a user cannot submit the form unitl all fields are complete with the required information
* Toggle switch - toggles the selected field on or off
* Submit button - directs the user to their profile page with a flash message of a successful recipe add
* Cancel button - directs the user back to their profile page

#### Profile Page

* Back button - directs the user back to the previous page they were on
* Add recipe button - directs the user to the add recipe page form
* Accordion header -
    * When clicked anywhere, it drops down to reveal the accordion content
    * Go to recipe button - directs the user to the recipe page of required recipe
    * Edit button - directs the user to the edit recipe form
    * Delete button - activates a modal to confirm removal recipe
        * Modal activated from delete button - gives the user two options -
            * Cancel button - cancels the request to delete and returns the user to the accordion of the profile page
            * Delete button - removes the recipe from the database completely, and returns the user to the profile page with a confirmation of removal flash message
    * Accordion body content - when viewd on smaller screens the edit, delete and go to rrecipe buttons from the head move to the body, with the same functionality as when in the head of the accordion.

#### Edit Recipe Page

* Back button - directs the user back to the previous page they were on
* Slider control buttons - allows the user to select with slider image to view, otherwise it changes automatically over time
* Edit recipe form - a user cannot submit the form unitl all fields are complete with the required information
* Toggle switch - toggles the selected field on or off
* Submit button - directs the user to their profile page with a flash message of a successful recipe add
* Cancel button - directs the user back to their profile page

#### Recipe Page

* Back button - directs the user back to the previous page they were on
* Edit button - directs the user to the edit recipe form
* Delete button - activates a modal to confirm removal recipe
    * Modal activated from delete button - gives the user two options -
        * Cancel button - cancels the request to delete and returns the user to the accordion of the profile page
        * Delete button - removes the recipe from the database completely, and returns the user to the profile page with a confirmation of removal flash message

#### Search Results Page

* Back button - directs the user back to the previous page they were on
* Slider control buttons - allows the user to select with slider image to view, otherwise it changes automatically over time
* Recipe card - directs the user to that specific recipes page

#### Bugs Found

Any bugs found during testing this site were all possible to fix. There were some where new code to be added, but the majority were simple syntax errors. DevTools had revealed most errors during that testing stage, but the manual testing was good as it was another final check before deployment.

* After a user registers to the site, they are directed to their profile page. If the user then clicked the back button it sent them back to the registeration form, despite just completing this action. I fixed this bug by included an if statement in the python code to control that if the user is in session, keep profile page rendered if the back button was clicked.

***

### User Testing

Once my project was nearly finsihed, minus the odd bug issue, I sent it out to be reviewed.

#### Peer-code-review

My project was submitted to the peer-code-review channel page of the Slack community for Code Institute. Unfortuantely I only had one reply for this project review submission, however it did poing out that some images and the logo of the side nav had broken links. I was able to fix these issues straight away as they were just simple mistakes in the way the code found the image.

#### User Review

My project was also sent out to various friends and family members to review the site thouroughly and read through the supporting documentation. I received feedback from people of different ages and professions and they notifyied me of any bugs and/or user experience issues. The general reviews of my page were positive, commenting on the general flow of the site, the colour scheme being attactive and fun to use when adding recipes to ones own profile page. The design of how the content was presented on the different screens was complemented along with how, despite the colourful content, the site didn't feel too cluttered.

### Further Testing

The website was tested on Google Chrome, Internet Explorer, Microsoft Edge, Mozilla Firefox and Safari browsers. It was viewed on a range of
different devices, such as desktop, laptops, iPhone 5S, iPhone 8 plus, iPhone 12 Pro, iPhoneX, iPad 2019, and Samsung Galaxy. Extensive testing was carried out to make sure the links were working correctly, and that the images loaded correctly.

