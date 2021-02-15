$(document).ready(function () {
    $(".sidenav").sidenav();
    $('.collapsible').collapsible();
    $('input#username, input#password, input#confirm-password').characterCounter();
    $('.slider').slider();
    $('select').formSelect();
    $('.modal').modal();

    /* Code taken from Code Institute lesson 'Materialize Form Validation' - 
    Code makes the dropdown section on the form a required field */

    validateMaterializeSelect();

    function validateMaterializeSelect() {
        var classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        var classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }

        });
    }

    /* Passwords don't match code found and taken
    from https://codepen.io/diegoleme/pen/surIK */

    var password = document.getElementById("password"),
        confirm_password = document.getElementById("confirm-password");

    function validatePassword() {
        if (password.value != confirm_password.value) {
            confirm_password.setCustomValidity("Passwords Don't Match");
        } else {
            confirm_password.setCustomValidity('');
        }
    }

    password.onchange = validatePassword;
    confirm_password.onkeyup = validatePassword;

});

/* Code taken from my MS2 project and edited.
Originally found on WS3 Schools.
https://www.w3schools.com/howto/howto_js_scroll_to_top.asp */

// Get the button

mybutton = document.getElementById("to-top-btn");

// When the user scrolls down 200px from the top of the document, show the button

window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document

function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

/* Code found on https://www.w3schools.com/jsref/met_his_back.asp */

function backButton() {
    window.history.back();
}