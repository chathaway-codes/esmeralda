from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

class HomePageTestCase(TestCase):
    def test_anon_access(self):
        res = self.client.get(reverse('home'))
        self.assertEquals(res.status_code, 200), "Failed to fetch homepage"
    def test_login_access(self):
        # Make the user we will use
        user = User.objects.create_user(username='test', password='test')
        user.save()
        res = self.client.login(username='test', password='test')
        self.assertEquals(res, True, "Failed to log in")
        res = self.client.get(reverse('home'))
        self.assertEquals(res.status_code, 200, "Failed to fetch homepage")
