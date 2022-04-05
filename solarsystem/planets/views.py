from django.shortcuts import render
from .models import SolarSystemObjects

def index(request):
    objects = SolarSystemObjects.objects.all()
    data = {
        'title': 'Главная страница',
        'objects': objects,
    }

    return render(request, "main/index.html", data)

def description(request):
    return render(request, "main/description.html")



