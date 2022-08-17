from . import views
from django.urls import path
  
urlpatterns = [
    #path('', views.ApiOverview, name='home'),
    path('all/', views.select_all, name='select_all'),
    path('signup/', views.signup, name='insert_seller'),
    path('update/<int:pk>/', views.update_seller, name='update_seller'),
    path('delete/<int:pk>/', views.delete_seller, name='delete_seller'),
    path('select/<int:pk>/', views.select_seller, name='select_seller'),
]