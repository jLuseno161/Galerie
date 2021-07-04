from la_galerie.models import Category, Image, Location
from django.shortcuts import render

# Create your views here.

def showpage(request):
    images = Image.objects.all()
    location=Location.get_locations()

    return render(request,'galeria.html',{"images":images,"location":location})
def search_category(request):

    location=Location.get_locations()

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        search = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'search.html',{"message":message,"category": search,"location":location})
    else:
        return render(request, 'search.html')

def image_properties(request,image_id):
    location=Location.get_locations()

    image = Image.get_image_by_id(image_id)
    return render(request, {"image" : image,"location":location})

def image_location(request,location_name):
    location=Location.get_locations()
    image= Image.fetch_by_location(location_name)
    message = f"{location_name}"
    return render(request, 'img_location.html',{"message":message,"image": image,"location":location})
   
