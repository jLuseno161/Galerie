from django.contrib import admin

# Register your models here.
from .models import Location, Image, Category

# Register your models here.
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)