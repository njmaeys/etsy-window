from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestPortalView(TestCase):
    def setUp(self):
        self.client = Client()
        self.portal_url = 'portal-home'
        self.login_url = 'login'

        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.user.save()

    def test_authenticated_user_can_access_portal(self):
        self.client.login(username='testuser', password='password123')

        response = self.client.get(reverse(self.portal_url))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Portal')
        self.assertEqual(response.context['user'], self.user)

    def test_unauthenticated_user_cannot_access_portal(self):
        response = self.client.get(reverse(self.portal_url))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/{self.login_url}/')
