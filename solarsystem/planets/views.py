from django.shortcuts import render, get_object_or_404
from .models import SolarSystemObjects

def index(request):
    objects = SolarSystemObjects.objects.all()
    data = {
        'title': 'Главная страница',
        'objects': objects,
    }

    return render(request, "main/index.html", data)

def description(request, object_name):
    object = get_object_or_404(SolarSystemObjects, object_name=object_name)
    return render(request, "main/description.html", {'object': object})



