/*jshint esversion: 6 */


/* 
    credit to https://docs.djangoproject.com/en/3.2/ref/csrf/
    gets csrf token
*/

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


/*
this code on submit of new message on chat form,
adds to database using ajax and on success appends the message to current chat window
if submit button is disabled we exit submit function
*/

$('#chat-form').on('submit', function (event) {
    event.preventDefault();

    if ($('#submit-button').hasClass('disabled')){
        return;
    }

    var message = $('#message').val();
    var url = $('#chat-form').attr('action');
    
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            message: message,
            csrfmiddlewaretoken: csrftoken
        },
        success: function (response) {
            var newdata = JSON.parse(response);
            $('#message').val('');
            var newmessage = newdata.message_content;
            var user = newdata.user_name;
            var insert = $(`
            <div class="card chat-card mb-3 mt-1 ml-3">
            <div class="card-body">
            <blockquote class="blockquote mb-0">
                <p class="card-text">${newmessage}</p>
                <footer class="blockquote-footer">${user}</footer>
            </blockquote>
            </div>
            </div>`);
            $('#chat-window').append(insert);
            $('#chat-window').scrollTop($('#chat-window')[0].scrollHeight);
        },
        error: (error) => {
            console.log(error);
        }
    });
});


/* check if new messages and append to chat window every minute */

setInterval(function () {
    checkChatMessages();
}, 60000);

function checkChatMessages(event) {
    event.preventDefault();
    var numOfChats = $('.chat-card').length;
    $.ajax({
        url: '/numberOfMessages/',
        type: 'POST',
        data: {
            numOfChats: numOfChats,
            csrfmiddlewaretoken: csrftoken
        },
        success: function (response) {
            if (response == 'up_to_date') {
                return;
            } else {
                var message = response;
                var insert = $(`
                <div class="card chat-card mb-3 mt-1 float-right mr-3">
                <div class="card-body">
                <blockquote class="blockquote mb-0">
                    <p class="card-text">${message}</p>
                    <footer class="blockquote-footer">Leticia</footer>
                </blockquote>
                </div>
                </div>`);
                $('#chat-window').append(insert);
                $('#chat-window').scrollTop($('#chat-window')[0].scrollHeight);
                var expanded = $('#button-chat').attr('aria-expanded');
                if (expanded == "false") {
                    $('#button-chat').addClass('green');
                    $('#button-chat').removeClass('purple');
                }
            }
        },
    });
}

/* on click removes the colour that was added for new message above 
and scrolls to buttom to show newest message */
$('.button-chat').on('click', function (event) {
    $('#button-chat').addClass('purple');
    $('#button-chat').removeClass('green');
    $('#chat-window').scrollTop($('#chat-window')[0].scrollHeight);
});

/* close alert window */
$('.close-window').on('click', function (event) {
    $('.message-container').addClass('d-none');
});

/* on expand on navbar for mobile change colour of backgorund using class change */
$(".navbar-toggler").click(function () {
    $(".navbar-collapse").toggleClass("nav-collapse-colour");
});
