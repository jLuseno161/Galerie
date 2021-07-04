from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=100)        

    def __str__(self):
        return self.location_name
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

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

class Image(models.Model):

    image_name =models.CharField(max_length=200)
    description =models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='0')
    location = models.ForeignKey(Location ,on_delete=models.CASCADE,default='0')
    image=models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def fetch_by_location(cls,location_name):
        location = cls.objects.filter(location__location_name = location_name).all()
        return location

    @classmethod
    def search_by_category(cls,category):
        image = cls.objects.filter(category__cat_name__icontains = category)
        return image

    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image

