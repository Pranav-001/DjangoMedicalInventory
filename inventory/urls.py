from . import views
from django.urls import path
  
urlpatterns = [
    #path('', views.ApiOverview, name='home'),
    path('all/', views.select_all, name='select_all'),
    path('all/', views.select_all, name='select_all'),
    path('insert/', views.insert_inventory, name='insert_inventory'),
]