from django.test import TestCase, Client
from django.urls import reverse


class TestContactView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_view(self):
        url = reverse('contact')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
