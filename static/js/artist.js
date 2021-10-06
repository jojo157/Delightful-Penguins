$('.status-button').on('click', function(event){
    event.preventDefault();
    var status = $(this).attr('id');
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

/*
$('.message-reply-button').on('click', function(event){
    event.preventDefault();
    var chat_session = $(this).attr('data-chat-session');
    var id = $(this).attr('data-chat-id');
    
    $.ajax({
        url: 'reply/',
        type: 'POST',
        data: {
            chat_session: chat_session,
            id: id,
            csrfmiddlewaretoken: document.querySelector('input[name="csrfmiddlewaretoken"]').value
        },
        success: function(response){
            data = JSON.parse(response);
            console.log("success");

           
        },
        error: (error) => {
            console.log(error);
        }
    }) 
});
*/

$('.message-reply-button').on('click', function(event){
    event.preventDefault();
    var chat_session = $(this).attr('data-chat-session');
    var id = $(this).attr('data-chat-id');

    var href = '/artist/reply';

    location.href = href + "/" + id ;

});
