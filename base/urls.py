from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='home'), # trigger the functions
]
