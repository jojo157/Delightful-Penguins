$('#chat-form').on('submit', function(event){
    event.preventDefault();
    var message = $('#message').val();
    var url = $('#chat-form').attr('action');
    $.ajax({
        url: url,
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


/* Functionality that on expand of chat box, stores the status in session storage.
This will be used on page reload to update the chat box attributes to match before reload */
$('.button-chat').on('click', function(event){
    var expanded = $(this).attr('aria-expanded');
    if (expanded == "false"){
        var newstate = "true";
        sessionStorage.setItem("expanded", newstate); 
    }
    else{
        sessionStorage.setItem("expanded", "false"); 
    }   
});

window.onload = function() {
    var expanded = sessionStorage.getItem("expanded");
        if(expanded == "true"){
        $('#button-chat').attr('aria-expanded', expanded);
        $('#collapseChat').addClass('show');
        FormPersistence.persist(form);  
    }
};

/* reload page every minute to allow chat box update */
/*
setTimeout('location.reload()', 60000);
*/

/* credit to FThompson for library to persist form data on reload https://github.com/FThompson/FormPersistence.js */
let form = document.getElementById('chat-form');
FormPersistence.persist(form);