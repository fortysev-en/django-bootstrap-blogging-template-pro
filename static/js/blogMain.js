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
  var username = document.getElementById('username').value
  var password = document.getElementById('password').value
  var csrf = document.getElementById('csrf').value

	if (username == "" || username.length < 5) {
		text = "Please enter a valid username!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	}
  if (password == "") {
		text = "Please enter a valid password!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	}
  else{
    var data = {
      'username' : username,
      'password' : password
    }
  
    fetch('/api/login/', {
      method : 'POST',
      headers : {
        'Content-Type' : 'application/json',
        'X-CSRFToken' : csrf,
      },
      body : JSON.stringify(data)
      
    }).then(result => result.json()).then(response =>{
          if (response.status == 200){
            window.location.reload('/')
            text = "Welcome <b>" + username + "</b>!";
            successText.innerHTML = text;
            var bsAlert = new bootstrap.Toast(successAlert);
            bsAlert.show();
          }
          else{
            response.message = text
            warningText.innerHTML = text;
            var bsAlert = new bootstrap.Toast(warningAlert);
            bsAlert.show();
          }
    })
  }
}

function signUp(){
    text = "Thank you for contacting me amigo, I'll surely contact you within a day!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
}