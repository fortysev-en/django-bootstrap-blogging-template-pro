// Defining Toasts
var successAlert = document.getElementById('success-toast');
var successText = document.getElementById("success-span");

var warningAlert = document.getElementById('warning-toast');
var warningText = document.getElementById("warning-span");

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

// show and hide password while changing the icon function
function togglePassword(){
    $("body").on('click', '.toggle', function() {
        $(this).toggleClass("bi bi-eye");
        var input = $("#password");
        if (input.attr("type") === "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
      });
}

function logIn(){
  text = "Please enter a valid name!";
  warningText.innerHTML = text;
  var bsAlert = new bootstrap.Toast(warningAlert);
  bsAlert.show();
}

function signUp(){
    text = "Thank you for contacting me amigo, I'll surely contact you within a day!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
}