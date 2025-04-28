from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('', views.home, name='home'),
]
