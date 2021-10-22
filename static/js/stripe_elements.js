/*jshint esversion: 6 */
const $ = window.$;

/* 
stripe card element for checkout page
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {
    style: style
});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


// Handle form submit

var form2 = document.getElementById('payment-form');

form2.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
    };
    var url = 'cache_checkout_data/';

    $.post(url, postData).done(function () {
        $('#submit-button2').attr('disabled', true);
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form2.full_name.value),
                    phone: $.trim(form2.phone_number.value),
                    email: $.trim(form2.email.value),
                    address: {
                        line1: $.trim(form2.street_address1.value),
                        line2: $.trim(form2.street_address2.value),
                        city: $.trim(form2.town_or_city.value),
                        country: $.trim(form2.country.value),
                        state: $.trim(form2.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form2.full_name.value),
                phone: $.trim(form2.phone_number.value),
                address: {
                    line1: $.trim(form2.street_address1.value),
                    line2: $.trim(form2.street_address2.value),
                    city: $.trim(form2.town_or_city.value),
                    country: $.trim(form2.country.value),
                    postal_code: $.trim(form2.postcode.value),
                    state: $.trim(form2.county.value),
                }
            },
        }).then(function (result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({
                    'disabled': false
                });
                $('#submit-button2').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form2.submit();
                }
            }
        });
    });
});