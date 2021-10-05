$('#chat-form').on('submit', function(event){
    event.preventDefault();
    var message = $('#message').val();
    $.ajax({
        url: '',
        type: 'POST',
        data: {
            message: message,
            csrfmiddlewaretoken: document.querySelector('input[name="csrfmiddlewaretoken"]').value
        },
        success: function(data){
            console.log('Success!');
            console.log(data);
        },
        error: (error) => {
            console.log(error);
        }
    }) 
});

