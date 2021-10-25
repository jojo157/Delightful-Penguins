from django.test import TestCase

class AllArtistViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='general', password='12test12', email='general@example.com')
        self.user.save()
        self.timestamp = date.today()
        self.client.login(username='general', password='12test12')
    
    def tearDown(self):
        self.user.delete()

    def test_only_artist_can_access_restricted_views(self):
        response = self.client.get('/artist')
        self.assertRedirects(response, '/')

    