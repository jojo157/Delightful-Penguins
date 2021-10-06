$('#chat-form').on('submit', function(event){
    event.preventDefault();
    var message = $('#message').val();
    $.ajax({
        url: 'chatSend/',
        type: 'POST',
        data: {
            message: message,
            csrfmiddlewaretoken: document.querySelector('input[name="csrfmiddlewaretoken"]').value
        },
        success: function(response){
            newdata = JSON.parse(response);
            $('#message').val('');
            newmessage = newdata["message_content"];
            user = newdata["user_name"];
            insert = $(`
            <div class="card mb-3 mt-1 ml-3">
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

