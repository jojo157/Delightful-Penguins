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
            console.log(data)
            $('#message').val("");
            var sentMessage =  `
            <div class="card mb-3 mt-1 ml-3">
                <div class="card-body">
                    <blockquote class="blockquote mb-0">
                        <p class="card-text">'content will go here'</p>
                        <footer class="blockquote-footer"></footer>
                    </blockquote>
                </div>
            </div>`;
            $('#chat-window').append(sentMessage);
        },
        error: (error) => {
            console.log(error);
        }
    }) 
});

