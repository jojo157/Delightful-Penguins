/*jshint esversion: 6 */


/* 
This code will update the artist status on click on button with id artist-status-switch
*/
$('#artist-status-switch').on('change', function (event) {
    var status = $(this).is(':checked');
    if (status == true) {
        status = "Online";
    } else {
        status = "Offline";
    }
    event.preventDefault();
    $.ajax({
        url: 'artist_status/',
        type: 'POST',
        data: {
            status: status,
            csrfmiddlewaretoken: document.querySelector('input[name="csrfmiddlewaretoken"]').value
        },
        success: function (response) {
            var message = "Messaging functionality is now" + " " + status;
            alert(message);
        },
        error: (error) => {
            console.log(error);
        }
    });
});


/*
This function on the click of a button with class message-reply-button
renders the reply view by getting its attribute for chat id and passing it
*/
$('.message-reply-button').on('click', function (event) {
    event.preventDefault();
    var id = $(this).attr('data-chat-id');
    var href = '/artist/reply';
    location.href = href + "/" + id;
});