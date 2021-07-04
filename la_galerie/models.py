from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=100)        

    def __str__(self):
        return self.location_name

    @classmethod
    def get_locations(cls):
        location = Location.objects.all()
        return location
        
class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    
