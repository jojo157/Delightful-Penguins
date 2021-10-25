from django.test import TestCase
from .models import Message, Artist, Contact
from .forms import ContactForm
from django.contrib.auth.models import User


class AllChatViewTest(TestCase):
    def test_can_send_message(self):
        response = self.client.post(
            "/chat/chatSend/",
            {"message": "send message test"},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        exists = Message.objects.filter(message_content="send message test")
        self.assertEqual(len(exists), 1)

    def test_can_access_contact_form_page(self):
        response = self.client.get("/chat/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

    def test_can_send_contact_email(self):
        form_data = {
            "name": "test",
            "email": "test@gmail.com",
            "mobile": "0851328804",
            "title": "test email",
            "contact_message": "test body",
        }
        response = self.client.post("/chat/contact/", form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "art.html")
