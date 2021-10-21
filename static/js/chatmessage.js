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
*/

$('#chat-form').on('submit', function (event) {
    event.preventDefault();
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
            newdata = JSON.parse(response);
            $('#message').val('');
            newmessage = newdata["message_content"];
            user = newdata["user_name"];
            insert = $(`
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
    })
});


/* Functionality that on expand of chat box, stores the status in session storage.
This will be used on page reload to update the chat box attributes to match before reload */
$('.button-chat').on('click', function (event) {
    var expanded = $(this).attr('aria-expanded');
    if (expanded == "false") {
        var newstate = "true";
        sessionStorage.setItem("expanded", newstate);
    } else {
        sessionStorage.setItem("expanded", "false");
    }
});

window.onload = function () {
    var expanded = sessionStorage.getItem("expanded");
    if (expanded == "true") {
        $('#button-chat').attr('aria-expanded', expanded);
        $('#collapseChat').addClass('show');
        FormPersistence.persist(form);
    }
};


/* check if new messages and append to chat window every minute */

setInterval(function () {
    checkChatMessages()
}, 60000);

function checkChatMessages() {
    var numOfChats = $('.chat-card').length;
    $.ajax({
        url: 'numberOfMessages/',
        type: 'POST',
        data: {
            numOfChats: numOfChats,
            csrfmiddlewaretoken: csrftoken
        },
        success: function (response) {
            if (response == 'up_to_date') {
                return;
            } else {
                message = response;
                insert = $(`
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
            }
        },
    })
}

/* close alert window */
$('.close-window').on('click', function (event) {
    $('.message-container').addClass('d-none');
});

/* on expand on navbar for mobile change colour of backgorund using class change */
$(".navbar-toggler").click(function () {
    $(".navbar-collapse").toggleClass("nav-collapse-colour");
})
