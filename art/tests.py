from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from chat.models import Message, Artist
from .models import Art
from .forms import ArtForm


class AllArtViewTest(TestCase):
    
    def test_landing_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "art.html")

    def test_add_art_loads_for_artist(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        response = self.client.get("/addArt/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "artAdd.html")

    def test_auth_user_cant_load_add_art(self):
        self.user = User.objects.create_user(
            username="general",
            password="12test12",
            email="general@example.com",
        )
        login = self.client.login(username="general", password="12test12")
        response = self.client.get("/addArt/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_add_art_adds_to_collection(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        form_data = {
            "name": "test art",
            "description": "test desc",
            "price": "20",
        }
        form = ArtForm(form_data)
        response = self.client.post("/addArt/", form_data)
        self.assertRedirects(response, "/")
        new_art = Art.objects.filter(name="test art")
        self.assertEqual(len(new_art), 1)

    def test_artist_can_delete_art(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        art = Art.objects.create(
            name="test art", description="test desc", price="20"
        )
        response = self.client.get(f"/deleteArt/{art.id}/")
        existing_art = Art.objects.filter(id=art.id)
        self.assertRedirects(response, "/")
        self.assertEqual(len(existing_art), 0)

    def test_art_detail_page_loads(self):
        art = Art.objects.create(
            name="test art", description="test desc", price="20"
        )
        response = self.client.get(f"/artDetails/{art.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "artDetails.html")

    def test_artist_can_view_edit_art(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        art = Art.objects.create(
            name="test art", description="test desc", price="20"
        )
        response = self.client.get(f"/editArt/{art.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "artEdit.html")

    def test_artist_can_edit_art(self):
        self.user = User.objects.create_superuser(
            username="super", password="12test12", email="super@example.com"
        )
        login = self.client.login(username="super", password="12test12")
        art = Art.objects.create(
            name="test art", description="test desc", price="20"
        )
        response = self.client.post(
            f"/editArt/{art.id}/",
            {"name": "new art", "description": "new desc test", "price": "50"},
        )
        self.assertRedirects(response, "/")
        new_art = Art.objects.get(id=art.id)
        self.assertEqual(new_art.name, "new art")
