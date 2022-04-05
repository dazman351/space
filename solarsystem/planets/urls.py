from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('description/', views.description, name='description'),
]