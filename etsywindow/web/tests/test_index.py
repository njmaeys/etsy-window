from django.test import TestCase, Client
from django.urls import reverse


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
