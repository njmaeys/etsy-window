from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.portal_url = reverse('portal-home')
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_with_valid_credentials(self):
        response = self.client.post(self.login_url, {'username': self.username, 'password': self.password})

        self.assertRedirects(response, self.portal_url)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(self.login_url, {'username': self.username, 'password': 'wrong_password'})

        self.assertContains(response, 'Invalid username or password')
