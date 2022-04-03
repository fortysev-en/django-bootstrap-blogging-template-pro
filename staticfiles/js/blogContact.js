// Defining Toasts
var successAlert = document.getElementById('success-toast');
var successText = document.getElementById("success-span");

var warningAlert = document.getElementById('warning-toast');
var warningText = document.getElementById("warning-span");



$(document).on('submit', '#contact-form', function(e){
	e.preventDefault();

	var name  = $('#name').val()
	var email = $('#email').val()
	var desc = $('#desc').val()
	var text;

	if (name == "" || name.length < 5) {
		text = "Please enter a valid name!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	}

	if (
		email == "" ||
		email.indexOf("@") == -1 ||
		email.length < 6
	) {
		text = "Please enter a valid email address!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	}

	if (desc == "" || desc.length <= 10) {
		text = "Some more information would be better!";
		warningText.innerHTML = text;
		var bsAlert = new bootstrap.Toast(warningAlert);
		bsAlert.show();
		return false;
	} else {
		$.ajax({
			type: 'POST',
			url: '',
			data: {
				name : name,
				email : email,
				desc : desc,
				csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
			},
			success: function(data){
				// $('.output').html(data);
				text = 'Thank you for reaching out \<b>'+ name +'</b>. I\'ll surely get back to you!';
				successText.innerHTML = text;
				var bsAlert = new bootstrap.Toast(successAlert);
				bsAlert.show();
				document.getElementById("contact-form").reset(); 
			
			}
		});
	}
});