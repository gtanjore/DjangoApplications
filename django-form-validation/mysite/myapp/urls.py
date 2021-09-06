from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('regform/', views.regform, name = 'registration form'),
]