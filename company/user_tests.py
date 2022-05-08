#Django Imports
from django.test import TestCase

#Our Custom Imports
from company.models import User

class userModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(
            username='testuser',
            email='test@gamil.com',
            password='secrete'
        )

    def test_name_label(self):
        #check if user created correctly
        self.assertTrue(User.objects.filter(username='testuser').exists())