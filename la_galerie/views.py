from la_galerie.models import Category, Image, Location
from django.shortcuts import render

# Create your views here.

def showpage(request):

    images = Image.objects.all()
    location=Location.objects.all()

    return render(request,'galeria.html',{"images":images,"location":location})

def search_category(request):

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        search = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'search.html',{"message":message,"category": search})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image_properties(request,image_id):

    image = Image.get_image_by_id(image_id)

    return render(request, {"image" : image})

def image_location(request,location_name):
    
    image= Image.fetch_by_location(location_name)

    return render(request,'img_location.html',{"image":image})

