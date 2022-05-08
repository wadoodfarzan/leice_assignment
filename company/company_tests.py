#Django Imports
from django.test import TestCase

#Our Custom Imports
from company.models import Company

class companyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Company.objects.create(name='Farzan Wadood Company',parent_id=1)

    def test_name_label(self):
        #test case to check table created in database
        company = Company.objects.get(id=1)
        field_label = company._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        company = Company.objects.get(id=1)
        max_length = company._meta.get_field('name').max_length
        self.assertEqual(max_length, 256)