from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestLogoutView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('logout')
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

    def test_logout_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('home'))

