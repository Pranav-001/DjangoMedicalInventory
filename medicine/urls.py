from . import views
from django.urls import path
  
urlpatterns = [
    #path('', views.ApiOverview, name='home'),
    path('all/', views.select_all_medicine, name='select_all_medicine'),
    path('insert/', views.insert_medicine, name='insert_medicine'),
    path('update/<int:pk>/', views.update_medicine, name='update_medicine'),
    path('delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
    path('select/<int:pk>/', views.select_medicine, name='select_medicine'),
    path('all_c/', views.select_all_chemical_compound, name='select_all_chemical_compound'),
    path('insert_c/', views.insert_chemical_compound, name='insert_chemical_compound'),
    path('upadate_c/<int:pk>/', views.update_chemical_compound, name='update_all_chemical_compound'),
    path('delete_c/<int:pk>/', views.delete_chemical_compound, name='delete_chemical_compound'),
    path('select_c/<int:pk>/', views.select_chemical_compound, name='select_chemical_compound'),
    
]