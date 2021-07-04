from django.test import TestCase
from .models import Image, Location, Category

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(cat_name='Nature')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0) 