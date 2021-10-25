from django.test import TestCase
from art.models import Art
from django.contrib.auth.models import User


class AllCartViewTest(TestCase):
    def setUp(self):
        Art.objects.create(
            name="test art", description="test desc", price="20"
        )

    def test_cart_page_loads(self):
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")

    def test_can_add_to_cart(self):
        art = Art.objects.get(name="test art")
        response = self.client.get(f"/cart/add_to_cart/{art.id}/")
        self.assertRedirects(response, "/cart/")
        session = self.client.session
        s_id = session["cart"]
        self.assertEqual(s_id[f"{art.id}"], art.id)
        self.assertEqual(len(s_id), 1)

    def test_can_remove_item_from_cart(self):
        art = Art.objects.get(name="test art")
        response1 = self.client.get(f"/cart/add_to_cart/{art.id}/")
        response = self.client.get(f"/cart/remove_cart_item/{art.id}/")
        self.assertRedirects(response, "/cart/")
        session = self.client.session
        s_id = session["cart"]
        self.assertEqual(len(s_id), 0)
