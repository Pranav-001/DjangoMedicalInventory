from . import views
from django.urls import path
  
urlpatterns = [
    #path('', views.ApiOverview, name='home'),
    path('all/', views.select_all, name='select_all'),
    path('insert/', views.insert, name='insert'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    path('select/<int:pk>/', views.select, name='select'),
]