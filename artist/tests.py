from django.test import TestCase
from django.contrib.auth.models import User
from chat.models import Message, Artist


class AllArtistViewTest(TestCase):
    def setUp(self):
        Message.objects.create(
            message_content="test message",
            user_name="general",
            chat_session="10.12.13.14.",
            reply_recieved="False",
        )
        Artist.objects.create(status="Offline")

    def test_auth_user_cant_access_artist_messages(self):
        self.user = User.objects.create_user(
            username="general",
            password="12test12",
            email="general@example.com",
        )
        login = self.client.login(username="general", password="12test12")
        response = self.client.get("/artist/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_auth_user_cant_access_customer_message(self):
        self.user = User.objects.create_user(
            username="general",
            password="12test12",
            email="general@example.com",
        )
        login = self.client.login(username="general", password="12test12")
        message = Message.objects.get(message_content="test message")
        response = self.client.get(f"/artist/reply/{message.id}/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_auth_user_cant_reply_as_artist(self):
        self.user = User.objects.create_user(
            username="general",
            password="12test12",
            email="general@example.com",
        )
        login = self.client.login(username="general", password="12test12")
        response = self.client.get("/artist/artist_send_reply/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_artist_can_access_artist_messages(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        response = self.client.get("/artist/")
        self.assertTemplateUsed(response, "artistMessages.html")

    def test_artist_can_reply_as_artist(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        message = Message.objects.get(message_content="test message")
        message_id = message.id
        response = self.client.post(
            "/artist/artist_send_reply/",
            {"message-id": message_id, "message-artist": "test reply"},
        )
        self.assertRedirects(response, "/artist/")
        reply_message = Message.objects.get(message_content="test message")
        self.assertEqual(reply_message.reply_recieved, True)

    def test_artist_can_update_artist_status(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        status = Artist.objects.get(status="Offline")
        response = self.client.post(
            "/artist/artist_status/",
            {"status": "Online"},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        new_status = Artist.objects.get(pk="1")
        self.assertEqual(new_status.status, "Online")
        self.assertEqual(response.status_code, 200)

    def test_artist_can_view_each_message(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        message = Message.objects.get(message_content="test message")
        response = self.client.get(f"/artist/reply/{message.id}/")
        self.assertTemplateUsed(response, "reply.html")
