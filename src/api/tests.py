from django.test import TestCase
from django.urls import reverse


class TestApiViews(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        result = response.json()
        assert result.get('foo') == 'bar'
