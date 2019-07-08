
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('register', views.register, name='register'),
    path('home',views.home, name="home"),
    path('delete/<list_id>',views.deleteItem, name="delete"),
    path('edit/<list_id>', views.edit, name="edit"),
    path('home/details/<list_id>', views.details, name="details"),
]
