from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('description/<str:object_name>', views.description, name='description'),
]