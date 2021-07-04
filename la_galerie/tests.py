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

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locat = Location.objects.all()
        self.assertTrue(len(locat) > 0) 

    def test_delete_location(self):
        self.location.delete_location()
        category = Location.objects.all()
        self.assertTrue(len(category) <= 0)
    
    def test_get_location(self):
        location = Location.get_locations()
        self.assertTrue(location)

class ImageTestClass(TestCase):

    def setUp(self):

        self.location = Location(location_name='Nairobi')
        self.location.save_location()

        self.category = Category(cat_name='Mountains')
        self.category.save_category()

        self.mountain= Image(id=1,image_name = 'Mountains', description ='Mountain Test',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.mountain,Image))
    
    def test_save_image(self):
        self.mountain.save_image()
        editors = Image.objects.all()
        self.assertTrue(len(editors) > 0)

