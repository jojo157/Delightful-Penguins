from django.test import TestCase
from django.contrib.auth.models import User


class AllOrderProfileViewTest(TestCase):
    def test_auth_user_can_access_order_history(self):
        self.user = User.objects.create_user(
            username="general",
            password="12test12",
            email="general@example.com",
        )
        login = self.client.login(username="general", password="12test12")
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders.html")

    def test_artist_can_access_all_orders(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        response = self.client.get("/profiles/all_orders/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders.html")

    def test_auth_user_cant_access_all_order(self):
        self.user = User.objects.create_user(
            username="general",
            password="12test12",
            email="general@example.com",
        )
        login = self.client.login(username="general", password="12test12")
        response = self.client.get("/profiles/all_orders/")
        self.assertRedirects(response, "/")
