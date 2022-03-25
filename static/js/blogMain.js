// Defining Toasts
var successAlert = document.getElementById('success-toast');
var successText = document.getElementById("success-span");

var warningAlert = document.getElementById('warning-toast');
var warningText = document.getElementById("warning-span");

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

$("#chtHead").click(function() {
  // $('#chatbar').toggleClass("slidein slideout");
  var elementClasses = document.getElementById("chatbar");
  var classesArr = elementClasses.classList;

  if(classesArr.value.includes("slideout"))  
  {  
    elementClasses.classList.remove("slideout");
    elementClasses.classList.add('slidein');
  }   
  else if (classesArr.value.includes("slidein"))
  {  
    elementClasses.classList.remove("slidein");
    elementClasses.classList.add('slideout');
  }
  else{
    elementClasses.classList.add('slideout');
  }

  // if (element.className != "slidein") {
  //   element.className = "newStyle";
  // } else {
  //   element.className = "myStyle";
  // }

  var scrollEnd = document.getElementById('innerContentBox');
  scrollEnd.scrollTop = scrollEnd.scrollHeight;
});


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

// show and hide password while changing the icon function
function toggleConfirmPassword(){
  $("body").on('click', '.toggle', function() {
      $(this).toggleClass("bi bi-eye");
      var input = $("#confirmPassword");
      if (input.attr("type") === "password") {
        input.attr("type", "text");
      } else {
        input.attr("type", "password");
      }
    });
}

function scrollTillBottom(){
  var scrollEnd = document.getElementById('innerContentBox');
  scrollEnd.scrollTop = scrollEnd.scrollHeight;
}

function logIn(){
  // event.preventDefault()
  var username = document.getElementById('username').value
  var password = document.getElementById('password').value
  var gReCaptcha = document.getElementById('g-recaptcha-response').value
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
      'password' : password,
      'gReCaptcha' : gReCaptcha
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
  var gReCaptcha = document.getElementById('g-recaptcha-response').value
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
      'email' : email,
      'gReCaptcha' : gReCaptcha
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

function blogComment(event){
  event.preventDefault();
  var postComment = document.getElementById('postComment').value
  var postId = document.getElementById('postId').value
  var csrf = document.getElementById('csrf').value

  if (postComment == ''){
    text = "Please enter a message!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
  }
  else{
    var data = {
      'postComment' : postComment,
      'postId' : postId
    }
  
    fetch('/api/comment/', {
      method : 'POST',
      headers : {
        'Content-Type' : 'application/json',
        'X-CSRFToken' : csrf,
      },
      body : JSON.stringify(data)
      
    }).then(result => result.json()).then(response =>{
          if (response.status == 200){
            $( "#innerContentBox" ).load(window.location.href + " #innerContentBox" );
            setTimeout(scrollTillBottom(), 1000)
            document.querySelector('input[name="postComment"]').value = '';
          }
          else{
            warningText.innerHTML = response.message;
            var bsAlert = new bootstrap.Toast(warningAlert);
            bsAlert.show();
          }
    })
  }
}


function deleteComment(event){
  event.preventDefault();
  var cmd = document.getElementById('userCommentID').value
  var csrf = document.getElementById('csrf').value

  // console.log(cmd)

  // var data = {
  //   'commentId' : cmd,
  // }

  // fetch('/api/deleteComment/', {
  //   method : 'POST',
  //   headers : {
  //     'Content-Type' : 'application/json',
  //     'X-CSRFToken' : csrf,
  //   },
  //   body : JSON.stringify(data)
    
  // }).then(result => result.json()).then(response =>{
  //       if (response.status == 200){
  //         $( "#innerContentBox" ).load(window.location.href + " #innerContentBox" );
  //       }
  //       else{
  //         warningText.innerHTML = response.message;
  //         var bsAlert = new bootstrap.Toast(warningAlert);
  //         bsAlert.show();
  //       }
  // })

  $( "#innerContentBox" ).load(window.location.href + " #innerContentBox" );
}




// var xmlHttp = new XMLHttpRequest();
// xmlHttp.open( "GET", 'https://api.quotable.io/random?tags=technology', false ); // false for synchronous request
// xmlHttp.send( null );

// let data = xmlHttp.responseText;
// let dataJSON = JSON.parse(data);
// console.log(dataJSON.content);
// console.log(dataJSON.author);

// document.getElementById('quote').innerHTML = dataJSON.content
// document.getElementById('author').innerHTML = dataJSON.author


