$(document).ready(function(){
    $(".sidenav").sidenav();
    $('.collapsible').collapsible();
    $('input#username, input#password, input#confirm-password').characterCounter();
    $('.slider').slider();
    $('select').formSelect();
  });

/* 
Passwords don't match
code found and taken from https://codepen.io/diegoleme/pen/surIK
*/

var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm-password");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;