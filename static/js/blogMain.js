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
            window.location.href = '/'
          }
          else{
            warningText.innerHTML = response.message;
            var bsAlert = new bootstrap.Toast(warningAlert);
            bsAlert.show();
          }
    })
  }
}

function signUp(){
  var firstname = document.getElementById('firstname').value
  var lastname = document.getElementById('lastname').value
  var email = document.getElementById('username').value
  var password = document.getElementById('password').value
  var confirmpassword = document.getElementById('confirmPassword').value
  var csrf = document.getElementById('csrf').value

	if (firstname == "" || lastname == "" || firstname.length < 2 || lastname.length < 2) {
		text = "Please enter a valid firstname or lastname!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	}
  if (email == "" || email.indexOf("@") == -1 || email.length < 6) {
		text = "Please enter a valid email address!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	}
  if (password == "" || password.length < 8) {
		text = "Password should be atleast 8 characters long!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	}
  if (password != confirmpassword) {
		text = "Confirm password does not match!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	}
  else{
    var data = {
      'firstname' : firstname,
      'lastname' : lastname,
      'username' : email,
      'password' : password,
      'email' : email
    }
  
    fetch('/api/signup/', {
      method : 'POST',
      headers : {
        'Content-Type' : 'application/json',
        'X-CSRFToken' : csrf,
      },
      body : JSON.stringify(data)
      
    }).then(result => result.json()).then(response =>{
          if (response.status == 200){
            $( "#signup-container" ).load(window.location.href + " #signup-container" );
              successText.innerHTML = response.message ;
              var toastDiv = document.getElementById('success-toast-with-img')
              var bsAlert = new bootstrap.Toast(toastDiv);
              bsAlert.show();
              // window.location.reload()  
          }
          else{
            warningText.innerHTML = response.message ;
            var bsAlert = new bootstrap.Toast(warningAlert);
            bsAlert.show();
            // window.location.reload()
          }
    })
  }
}

// function searchBar(){

//   searchQuery = document.getElementById('serchField').value

//   console.log(searchQuery)

//   $.ajax({
//     // points to the url where your data will be posted
//     url:'/',
//     // post for security reason
//     type: "GET",
//     // data that you will like to return 
//     data: {'searchQuery' : searchQuery},
//     // what to do when the call is success 
//     success:function(response){
//       console.log('SUCCESS')
//       $( "#src" ).load(window.location.href + " #src" );
//     },
//     // what to do when the call is complete ( you can right your clean from code here)
//     complete:function(){},
//     // what to do when there is an error
//     error:function (xhr, textStatus, thrownError){
//       console.log('FAIL')
//     }
// });

// }




// var xmlHttp = new XMLHttpRequest();
// xmlHttp.open( "GET", 'https://api.quotable.io/random?tags=technology', false ); // false for synchronous request
// xmlHttp.send( null );

// let data = xmlHttp.responseText;
// let dataJSON = JSON.parse(data);
// console.log(dataJSON.content);
// console.log(dataJSON.author);

// document.getElementById('quote').innerHTML = dataJSON.content
// document.getElementById('author').innerHTML = dataJSON.author


