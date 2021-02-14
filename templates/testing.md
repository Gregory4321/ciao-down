# Testing
[back to README.md file](https://github.com/Gregory4321/ciao-down/blob/master/README.md)

## Table of Contents:
* [Validators](#validators)
    * [W3C Validators](#w3c-validators)
    * [JSHint Validator](#jshint-validator)
    * [PEP8](#pep8)
* [DevTools](#devtools)
* [Site Testing](#site-testing)
    * [User Stories from User Experince (UX) Section](#user-stories-from-user-experience-(ux)-section)
        * [First Time Visitor Goals](#first-time-visitor-goals)
    * [User Testing](#user-testing)
        * [Peer Code Review](peer-code-review)
        * [User Review](user-review)
    * [Further Testing](#further-testing)

***

Testing this site was conducted using various methods to identify any bugs throughout the site. I tested thoroughly throughout building the site, and when the build was completed. I used automatic testing in the form of W3C Validators, JSHint, and PEP8.

## W3C Validators

The W3C Markup Validator and W3C CSS Validator Services were used to validate the code on all of the pages and to make sure that there were no syntax errors in the project. Both the HTML and CSS code were run through these services regularly during the building of this project to ensure the code was valid throughout the process and to avoid nasty suprises at the end.

* [W3C Markup Validator](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### HTML

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

### CSS

Passing my script.css file through the it passed with no errors.

[CSS Validation Passed](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/css-validation.png)

## JSHint Validator

* [JSHint](https://jshint.com/)

The JSHint validator was used to pass the JS code through and increase the code quality and detect any potential bugs. It pointed out 'let' was available in ES6 (use 'esversion: 6'). I was able to easily recify this problem by using 'var' instead of 'let'.
It also showed what variables were unused or undefined. The undefined variables was just returning the '$' from the jQuery used from materialize and other code. The unused variables realted to the top button and back button. I believe these warnings can be overlooked as the code works fine. I decided not to make any changes to these errors.

[Unused variable error](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/vars-unused.png)

## PEP8

My python file was passed through the [PEP8](http://pep8online.com/) validator. Is passed with no problems. I believe this was due to the fact that the linter installed on my chosen IDE made me keep my code PEP8 compliant whilst writing the code, by throwing visual linting errors.

[Python Validation Passed](https://github.com/Gregory4321/ciao-down/blob/master/static/readme_images/testing_images/python-validation.png)

***
