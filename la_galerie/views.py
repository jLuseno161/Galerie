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
