from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=100)        

    def __str__(self):
        return self.location_name

    @classmethod
    def get_locations(cls):
        location = Location.objects.all()
        return location
    