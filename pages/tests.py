from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView


class Home_Page_Tests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertContains(self.response, 'Home')
        self.assertNotContains(self.response, 'This should not be there!')
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


