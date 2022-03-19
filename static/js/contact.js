// Defining Alerts
var green_inner_html = document.querySelector(".green-inner-alert-msg");
var red_inner_html = document.querySelector(".red-inner-alert-msg");
const green_div = document.querySelector(".alert-popup-green");
const red_div = document.querySelector(".alert-popup-red");


$(document).on('submit', '#contact-form', function(e){
	e.preventDefault();

	var name  = $('#name').val()
	var email = $('#email').val()
	var desc = $('#desc').val()
	var text;

	if (name == "" || name.length < 5) {
		text = "Please enter a valid name!";
		red_inner_html.innerHTML = text;
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

	if (desc == "" || desc.length <= 10) {
		text = "Some more information would be better!";
		red_inner_html.innerHTML = text;
		red_div.style.display = "block";
		setTimeout(function () {
			red_div.style.display = "none";
		}, 5000);
		return false;
	} else {
		$.ajax({
			type: 'POST',
			url: 'portfolio/contact',
			data: {
				name : name,
				email : email,
				desc : desc,
				csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
			},
			success: function(data){
				// $('.output').html(data);
				text = 'Thank you for reaching out \<b>'+ name +'</b>. I\'ll surely get back to you!';
				green_inner_html.innerHTML = text;
				green_div.style.display = "block";
				setTimeout(function () {
					green_div.style.display = "none";
				}, 5000);
				document.getElementById("contact-form").reset(); 
			
			}
		});
	}
});