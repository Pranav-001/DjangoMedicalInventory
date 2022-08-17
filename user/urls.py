from . import views
from django.urls import path
  
urlpatterns = [
    #path('', views.ApiOverview, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('all/', views.select_all, name='select_all'),
    path('select/<int:pk>/', views.select_user, name='Select_user'),
    path('delete/<int:pk>/', views.delete_user, name='delete_user'),
    path('update/<int:pk>/', views.update_user, name='update_user'),
]