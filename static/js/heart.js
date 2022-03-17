document.querySelectorAll('.heart').forEach(button => button.addEventListener('click', e => button.classList.toggle('active')));
// document.getElementById('btn-heart').classList.add('active');
$(document).on('submit', '#heart', function(e){
	e.preventDefault();

    // var classList = document.getElementById("btn-heart").classList;
    
    // for(var i = 0; i < classList.length; i++){
    //     console.log(classList[i]);
    // }

    $.ajax({
        type: 'POST',
        url: '/temp',
        data: {
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(data){
            // $('.output').html(data);
            console.log('Hell');
        }
    });
	
});
