from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),

    path('show/',views.show),  
    path('addemployee/', views.addemployee),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]