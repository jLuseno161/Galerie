from la_galerie.models import Category, Image, Location
from django.shortcuts import render

# Create your views here.

def showpage(request):

    images = Image.objects.all()
    location=Location.objects.all()

    return render(request,'galeria.html',{"images":images,"location":location})
