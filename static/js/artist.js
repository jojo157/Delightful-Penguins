$('.status-button').on('click', function(event){
    event.preventDefault();
    var status = $(this).attr('id');
    var action = $(this).attr('href');
    $.ajax({
        url: 'artist_status/',
        type: 'POST',
        data: {
            status: status,
            csrfmiddlewaretoken: document.querySelector('input[name="csrfmiddlewaretoken"]').value
        },
        success: function(response){
           message = "Messaging functionality is now" + " " + status ; 
           alert(message);
        },
        error: (error) => {
            console.log(error);
        }
    }) 
});
 
 


