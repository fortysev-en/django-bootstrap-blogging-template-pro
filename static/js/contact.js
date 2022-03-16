document.getElementById("contact-form").addEventListener("submit", portfolioContact);
// Defining Alerts
var green_inner_html = document.querySelector(".green-inner-alert-msg");
var red_inner_html = document.querySelector(".red-inner-alert-msg");
const green_div = document.querySelector(".alert-popup-green");
const red_div = document.querySelector(".alert-popup-red");

function portfolioContact(event) {
	var suggmessagesRef = firebase.database().ref("Portfolio Contact Form/" + date);

	event.preventDefault();

	var email = getInputVal("email");
	var name = getInputVal("name");
	var message = getInputVal("desc");
	var resetForm = document.getElementById("contact-form");
	var text;

	if (name == "" || name.length < 5) {
		text = "Please enter a valid name!";
		red_inner_html.innerHTML = text;s
		red_div.style.display = "block";
		setTimeout(function () {
			red_div.style.display = "none";
		}, 5000);
		return false;
	}

	if (
		email == "" ||
		email.indexOf("@") == -1 ||
		email.length < 6
	) {
		text = "Please enter a valid email address!";
		red_inner_html.innerHTML = text;
		red_div.style.display = "block";
		setTimeout(function () {
			red_div.style.display = "none";
		}, 5000);
		return false;
	}

	if (message == "" || message.length <= 10) {
		text = "Some more information would be better!";
		red_inner_html.innerHTML = text;
		red_div.style.display = "block";
		setTimeout(function () {
			red_div.style.display = "none";
		}, 5000);
		return false;
	} else {
		saveMessage(email, name, message);
		resetForm.reset();
		text = "Thank you for reaching out to me. I'll get back to you within 48 hours!";
		green_inner_html.innerHTML = text;
		green_div.style.display = "block";
		setTimeout(function () {
			green_div.style.display = "none";
		}, 5000);
	}

	// Function to get get form values
	function getInputVal(id) {
	return document.getElementById(id).value;
	}

	// Save message to firebase
	function saveMessage(email, name, message) {
		// var newsuggMessageRef = suggmessagesRef.push();
		// newsuggMessageRef.set({
		// 	Name: portname,
		// 	Email: portemail,
		// 	Message: portmessage,
		// 	Date: dateTime
		// });
        console.log(email, name, message)
	}
}