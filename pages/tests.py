from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView
from .models import Attack, Defence


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


class Model_Testing(TestCase):

    def setUp(self):
        self.attack = Attack.objects.create(
            operators='Fuze-test',
        )
        self.defence = Defence.objects.create(
            operators='Smoke',
        )

    def test_models(self):
        a = self.attack
        d = self.defence
        self.assertTrue(isinstance(a, Attack))
        self.assertEqual(str(a), 'Fuze')
        self.assertTrue(isinstance(d, Defence))
        self.assertEqual(str(d), 'Smoke')
