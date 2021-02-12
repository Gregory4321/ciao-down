# Milestone Project 3 - Ciao Down
View live project <a href=“https://ciao-down.herokuapp.com/”>here</a>

![Ciao Down Am I Responsive image](#)

Ciao Down is a free to use online cookbook app focused on Italian cuisine, that presents the user with recipes that have been shared on the
site. The user is able to create a free account. Doing so give them the ability to add their own recipes to the site, edit those
recipes, and delete those recipes if wanted.

***
## Table of Contents:
* [What does it do and what does it need to fulfill?](#what-does-it-do-and-what-does-it-need-to-fulfill)
* [User Experience](#user-experience)
   * [User Stories](#user-stories)
   * [Design](#design)
       * [1. Colour Scheme](#1-color-scheme)
       * [2. Font](#2-font)
       * [3. Logo](#3-logo)
       * [4. Geometry](#4-geometry)
       * [5. Wireframes](#5-wireframes)
* [Technologies Used](#technologies-used)
* [Features](#features)
   * [Existing Features](#future-features)
   * [Future Features](#removed-features)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Hosting on Github Pages](#hosting-on-github-pages)
    * [Running Project Locally](#running-project-locally)
* [Credits](#credits)
    * [Content](#content)
    * [Code](#code)
    * [Media](#media)
* [Acknowledgements](#acknowledgements)
* [Special Thanks](#special-thanks)
* [Disclaimer](#disclaimer)
***

## ![Ciao Down Logo](static/images/logo.png)

### Ciao Down Logo

<details>
<summary>Fun Fact?!</summary>
Ciao Down originated from a pun. 'Chow Down', means to eat down and enjoy one's food. This was morphed with the Italian word 'Ciao' to give the site the feel of Italian cuisine.
</details>

***

## **What does it do and what does it need to fulfill?**
This is my third milestone project where I have designed, created and built a fully Mobile Responsive CRUD Web Application for users to
store and share recipes. The project was built  with HTML, CSS, JavaScript, jQuery, Python, Flask, and MongoDB. The Materialize Framework was
used along side these programming languages to help give the site a clear strucutre and ensure the site is as responsive as possible for use
across various screen sizes, including desktop, tablet and mobile.
Users will be able to register, see their profile, log out and log back in again. Registered users will be able to add new recipes, and use
a toggle switch to show if a recipe is Gluten Free or Vegetarian. Registered users will be able to edit and delete their own recipes.<br>

My goal was to create a recipe site where users could easily browse Italian cuisine and access clear and concise recipes. Many of the
recipe websites that I came across during my research required the user to scroll through lots of content before finding their desired
recipe. I felt this kind of design was too busy and could easily overwhelm the user. In order to enhance user experience, it was important
to me that the recipe pages on 'Ciao Down' displayed information (e.g: ingredients, method and dietary requirements) in a simple and
easy-to-digest manner. The target audience for this application is anyone who has an interest or passion for Italian food, not matter what
their age or experience.

## **User Experience**

### User Stories:

* Generic User:

    * As a user, I want to be able to navigate through the entire site, comfortably and securely.
    * As a user, I want to be able to easily search for recipes by name or ingredients.
    * As a user, I want to view the contents of recipes on the site.
    * As a user, I want to have the possibility of printing a recipe.
    * As a user, I want to be able to register/sign-up and create my own account on the site.

* Registered User:

    * As a registered user, I want to be able to easily log in to my account.
    * As a registered user, I want to be able to create and submit my own recipes to the site.
    * As a registered user, I want to be able to see my own recipes in one place.
    * As a registered user, I want to be able to easily edit my own recipes.
    * As a registered user, I want to be able to easily delete my own recipes.
    * As a registered user, I want to be able to add ingredients from a recipe to my shopping list in my profile.
    * As a registered user, I want to be able to easily edit my shopping list.
    * As a registered user, I want to be able to print my own shopping list.
    * As a registered user, I want to be able to easily log out of my account.

* Site admin:

    * As the site admin, I want to be able to do all that is possible for a generic user and registered user.
    * As the site admin, I want to be able to access ALL recipes on the site, having the abilitly to edit any errors found, and delete
    recipes in case of unsuitable content.
    * As the site admin, I want to be able to add new categories to the site as the site expands.
    * As the site admin, I want to be able to edit and remove categories as I see fit for user experience.

[Back to Top](#table-of-contents)

### Design
#### 1. Colour Scheme

The colour scheme used for this site was to be colourful and eyecatching, but also not overwhelming to the user. In order to keep the theme of my site clear, I decided to base my colour scheme on the Italian flag. I used [Coolors](https://coolors.co/) to start playing with
variations of green and red. It was important to me that the colour scheme didn't make the page feel to busy and cluttered, as the content of the site would be very colourful.

The colours I used are:

![Colour scheme](static/readme_images/colours.png)

The primary colour, Russian Green, was used for the navigation bar, buttons of forms and the back to top button, and some text on the recipe page for clearer contrast. I toned down the green to a slightly more muted shade that wasnt too garish, and easy on the eye and comforting for the user. It also worked well as the content of the page was going to be predominently colourful. Using the colour tool that appears when hovering over a colour set in the style.css page, I made the green a bit more bold for use as the colour of success flash messages, so it stood out clear to the user from the navbar. This colour was the GO Green.

I chose the background colour to be White, so that the colourful content of the page would be easily seen, and gave a clean break between areas of the pages. I was hesitant of using a white background as feedback from my Milestone Project 1 was about having text on a white background. I chose the white as I was wanting to use the Italian flag as my colour scheme, but also a lot of the sites I found when researching for this project used white backgrounds. 

The hamburger and home icons as well as the Log In/Sign Up/Logout text in the navbar looked cleaner as white text.

The red, International Orange Engineering was a bright colour and picked as an accent to contrast well with the white and green, breaking the page up, clearly defining the different sections of the page. Also completing my Italian flag design. It was used as the footer colour, and incorporated with the social icons that turned white on hover and the icon itself red, giving a very clear contrast for user experience. I also used the method of the colour tool mentioned above to get a brighter red to use as the error colour of flash messages, to really indicate the error to the user. This colour was the Imperial Red.

As mentioned above, receiving critcism of text on a white background, I gave the forms the background colour of Cultured. This gave a clear definition of the form itself, making it clear that this was the content, and keeping it user friendly. I discovered this colour using the tool as mentioned before, getting the right shade I wanted.

For text across the site, for the most part I used Black, to make sure all the words were clear and easy to read.

#### 2. Font

I found fonts from researching online cookbook reccomendations, and scouring [Google Fonts](https://fonts.google.com/), using their inbuilt compare tool. I decided to use two fonts throughout my site. I wanted the main and secondary fonts to complement each other well throughout the site.
The font for the body text was 'Source Sans Pro', which was a clean and easy to read font across all areas it was presented. I found this font bold and to the point, and stood out clearly when used as an overlay to images.The second font I used was 'Average'. This was not average as it's name may suggest. It was a Serif font that gave a bold statement when being used for headers and titles, that this was a statement. 
These fonts were included in the site by inserting an _import_ link of the Google Fonts API into the top of my style.css file. Both of the fonts had a fall back of 'Sans-serif', should the site not load the import correctly. 

#### 3. Logo

The logo was created using an online design tool called [Canva](https://www.canva.com/en_gb/). I started by creating a custom canvas to suit my required dimensions, and then set the background to the colour, Russian Green, so it would blend with the nav bar. I played with several combinations of hand written and block fonts until I found a combiation I was happy with. I wanted the two words to be in contrasting fonts. I then played with positioning to make it look more exciting, and then completed it with an underlying Italian flag. 

#### 4. Composition

There is a clear structure throughout the site. Each page had a fixed navbar and footer that was consistent and the ease of navigation across the site was enhanced further with back buttons and call to action buttons. A side nav was used to house the nav links to keep the site clean and keep the user interacting with the site, but not to the point of confusing the user. Content hinting was used on the home page to encourage the user to scroll down the page. A bact to top button also aided ease of use for the user once they had scrolled down, to avoid having to scroll all the way back to the top to find the navigation.I used containers across the pages to keep good margins and to avoid ay content being lost of the screen. Images were displayed in grids for clear and clean design for the user, and the use of an accordion on the users profile page kept text nicely bundled together in their own compartments.

#### 5. Wireframes

Having researched and thought over the design process thoroughly, I created a workspace on [Figma](https://www.figma.com/). I had initially sketched ideas onto paper, so now I could start to bring them to life. I created all the pages I had planned for desktop and mobile screen sizes, clearly showing how the structure of the content would mould together on the different sizes, creating more enhanced wireframes. The final pages I ended up with did not vary too much from the wirefrmaes I made during the palnning stages. There were some basic design choices I decided whilst constructing the pages that differ slightly from these wireframes. Find the links to these wireframes below.

<details>
<summary>Wireframes</summary>

* Home Page
    * [Desktop View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/home-wire.png)
    * [Mobile View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/mob-home-wire.png)
* Recipe Page
    * [Desktop View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/recipe-wire.png)
    * [Mobile View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/mob-recipe-wire.png)
* Profile Page
    * [Desktop View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/profile-wire.png)
    * [Mobile View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/mob-profile-wire.png)
* Add Recipe Page
    * [Desktop View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/add-wire.png)
    * [Mobile View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/mob-add-wire.png)
* Edit Recipe Page
    * [Desktop View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/edit-wire.png)
    * [Mobile View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/mob-edit-wire.png)
* Login Page
    * [Desktop View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/login-wire.png)
    * [Mobile View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/mob-login-wire.png)
* Registration Page
    * [Desktop View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/register-wire.png)
    * [Mobile View](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/wireframes/mob-register-wire.png)
</details>

[Back to Top](#table-of-contents)

***

## **Technologies Used**

### Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML5) - Language used to create the structure of the pages.

* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Language used to add styling across all pages.

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Language used to create interactivity across the pages.

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Language used to create the back-end functionality of the app.

* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - this templating language was used with the Flask Framework across the HTML pages. It extended the base.html page across all pages, sharing the header and footer, along with all the meta data and links needed for the page creations, especially the crucial !DOCTYPE html.

### Libraries, Frameworks and Editors

* [Materialize 1.0.0](https://materializecss.com/) - used as the base structure and layout of the site, using its grid system to aid responsiveness across screen sizes. Many components such as the navbar, footer and cards were used. Materialize jQuery was used for initialization of many components such as the sidenav, dropdown and modal

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - a micro-framework used to help with writing the Python code.

* [MongoDB](https://www.mongodb.com/) - the non-relational database used to store my data on it's cloud servers.

* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - used their WSGI toolkit for utilities to aid security of user's passwords.

* [Google Fonts](https://fonts.google.com/) - used to import the 'Source Sans Pro' and 'Average' fonts, that were used across all pages.

* [Font Awesome](https://fontawesome.com/) - used for their free range of icons.

* [PyMongo](https://pypi.org/project/pymongo/) - used as Python's API for MongoDB, to enable data links from the back-end to front-end.

* [Favicon.io](https://favicon.io/) - was used to generate the favicon image.

* [Gitpod](https://www.gitpod.io/) - used as preferred choice of IDE for writing my code.

* [Git](https://git-scm.com/) - used for version control by making use of the Gitpod terminal to add, commit and push to Github.

* [Github](https://github.com) - used to host the project's repository and store the code, and linked to Heroku to push latest changes to the deployed build version.

* [Heroku](https://www.heroku.com/) - used as a hosting platform for deploying my live version of this CRUD application.

* [Unsplash](https://unsplash.com/) - used to find images for use across the site.

* [Pexels](https://www.pexels.com/) - used to find images for use across the site.

* [Pixbay](https://pixabay.com/) - used to find images for use across the site.

* [Google Images](https://google.com) - used to find images for use across the site.

### Tools

* [Google](https://www.google.co.uk/) - used for researching various techniques, styles and information.

* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - used for testing and debugging.

* [Figma](https://www.figma.com/) - used for creating the wireframes in the design stage.

* [Coolors](https://coolors.co/) - used to find and compare colours that complimented one another, retrieve names of colours, and showcase
the colours on the README.md file as an image.

* [Canva](https://www.canva.com/) - used to design and create the logo and favicon logo.

* [Picresize](https://picresize.com/) - used to resize and crop images for better implementation, such as 25% or 50% smaller.

* [Am I Responsive](http://ami.responsivedesign.is/) - used for showing the responsiveness of the site across different screen sizes and providing the image at the top of this document.

* [Free Online HTML Formatter](https://www.freeformatter.com/html-formatter.html#ad-output) - used to format the HTML code in a neater and more organised fashion.

* [Free Online CSS Formatter](https://www.freeformatter.com/css-beautifier.html) - used to format the CSS code in a neater and more organised fashion.

* [Free Online JS Formatter](https://www.freeformatter.com/javascript-beautifier.html) - used to format the JavaScript code in a neater and more organised fashion.

***

## **Features**

### Features Across All Pages

All pages consist of a fixed navbar and footer, appropriate flash messages and back to top button. All pages other than the log in and sign up pages also contain a back button the previous URL.

#### Navbar

The nav is consistent across all pages, designed to be responsive to the different screen sizes. It is also fixed so always visible to the user.

* The logo is set to the center of the page, and also at the top of the sidenav. It is a link back to the home page.
* A home icon is displayed also for ease of navigation.
* Log in / Sign up is presented to a user, taking them to the corresponding pages.
* A hamburger icon reveals a sidenav, containing links to home, login, sign up pages, and a categories dropdown of 'All, Starters, Mains and Desserts'. This is the main navigation of the site.
* Once a user is signed in, the login / sign up of the navbar and sidenav menu are replaced with logout.
* In the side nav, a logged in user is also displayed with a profile and add recipe link.

#### Footer

* Users will find clickable social icons linking to the corresponding social media pages.

#### Flash messages

* Flash messages are displayed to the user depending on what action they have undertaken.
* The message will be displayed on the pages where it is obvious for the user to see that they are being notified of their actions
* If it is a successful action, such as adding recipe or logging in, the flash message will be displayed in green.
* If the action is unsuccessful, then an error color of red will be displayed, and/or for deletion of a recipe.

#### Back to Top button

* A back to top button is displayed to the user across all pages when the user scrolls down past 200px.

***

### Other Features


#### Home Page

The home page offers the user a few features.

* A user is firstly presented with a colourful hero image, an overlapping search bar, and content hinting below.
* A user can use the search bar to search for a recipe by name, or a key word from the recipe.
* Below the hero image is a hoverable grid, displaying featured recipes randomly generated from the database, all clickable taking them to each recipe.

#### Log in

The log in page displayes a slider of images at the top, and a log in form.

* The slider of images contains colourful images to inspire the user.
* Encouraging taglines welcome the user back, and to continue their story.
* If a user tries to submit an incorrect details, they are given an error flash message.
* If this visit is the users first time, they are provided with a link below the form to sign up.

#### Sign Up

Similar to the login page design, just a more complex form and different taglines.

* Taglines of encouragment to start their journey.
* Required fields will stop the user inputting empty or incorrect fields.
* If a user enters a username that already exists on the databse, then they are given an error flash message.
* If this visit is of a returning user, they are provided with a link below the form to log in.

#### Profile

This page is provided for the user to clearly see their submitted recipes. Only registered users can see this page

* Upon signing up or logging in, a user is taken to this page with a welcome flash message.
* If no recipes have been added, a user is notified of this, and offered the option to add a recipe.
* If there are submitted recipes, an accordion is displayed to the user.
* The accordion title provides the recipes title, a link to go to the recipe, and edit/delete buttons.
* The accordion body gives the category name, recipe description, and the date it was added.
* Being made responsive, when the screen size hits a certain breakpoint the edit/delete buttons move into the accordion body, to east with the transition of the changing screen size.

#### Add Recipe

* This page contains a form for the user to complete, adding a recipe to the database.
* All fields are required, and helper text is placed for advice.
* A user also has the ability to use toggle switches if a recipe is vegetarian or gluten free.
* If the user has changed their mind, they can hit the canel button, taking them back to their profile page.
* Once a user submits their recipe, they are directed to that recipes page, and a flash message confirming a successful add.

#### Edit Recipe
* This page is very similar to the add recipe page, same layout and buttons.
* The form os prefilld with the data of the recipe the user has chosen to edit.
* As like when adding a recipe, the user can either cancel this decision to edit, or submit.
* Upon submission they are taken to that recipes page with a success flash message.

#### Recipes Category Pages

* This page has a similar layour to the home page.
* A slider of images presents mouth watering images and the title of the selected category is displayed beneath.
* All images are displayed in a grid format as cards, responsive to the different screen sizes.
* Upon hovering over the cards, the recipe title is displayed.*
 Upon clicking the card, the user is directed to that recipe.

#### Recipe Page

* This page displays all the information in a clean and clear format of an added recipe.
* If a user is viewing their own recipe, they are given the option to edit or delete the recipe.
* This option is very handy for when a user first submits their recipe, and are taken to this page, they may discover a typo mistake.

***

### Future Features

#### Profile Page

* I initially had designed for a shopping list hosted on their profile page. This shopping list would be a styled accordion where the body would contain the user's shopping list of ingredients. There were to be buttons where the user could edit or delete each ingredient. This would of demonstrated further the knowledge and use of CRUD operations. From the recipe page, a user would have had the abilitly to add the ingreditns list to their own shopping list, where they could then tailor quanities to their own preferences. The user would have been able to manually add more ingredients to their list too from the accordion in their profile.
* Perhaps an extension of the users profile page, and/or an account page, where the user has the abilitly to change their username and password, email account associated with the account, and delete thri profile if wanted.