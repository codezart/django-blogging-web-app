from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Blogg-home"),
    path('about', views.about, name="Blogg-about"),
]