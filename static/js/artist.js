$('#artist-status-switch').on('change', function(event) {
    var status = $(this).is(':checked');
    if (status == true) {
        status = "Online"
    } else {
        status = "Offline"
    }
    event.preventDefault();
    $.ajax({
        url: 'artist_status/',
        type: 'POST',
        data: {
            status: status,
            csrfmiddlewaretoken: document.querySelector('input[name="csrfmiddlewaretoken"]').value
        },
        success: function(response) {
            message = "Messaging functionality is now" + " " + status;
            alert(message);
        },
        error: (error) => {
            console.log(error);
        }
    })
});




$('.status-button').on('click', function(event) {
    event.preventDefault();
    current = $(this);
    var status = $(this).attr('id');
    $.ajax({
        url: 'artist_status/',
        type: 'POST',
        data: {
            status: status,
            csrfmiddlewaretoken: document.querySelector('input[name="csrfmiddlewaretoken"]').value
        },
        success: function(response) {
            message = "Messaging functionality is now" + " " + status;
            $('.status-button').removeClass('btn-success');
            $('.status-button').addClass('btn-primary');
            current.removeClass('btn-primary');
            current.addClass('btn-success');
            alert(message);
        },
        error: (error) => {
            console.log(error);
        }
    })
});


$('.message-reply-button').on('click', function(event) {
    event.preventDefault();
    var chat_session = $(this).attr('data-chat-session');
    var id = $(this).attr('data-chat-id');

    var href = '/artist/reply';

    location.href = href + "/" + id;

});