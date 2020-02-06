
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete_checked/', views.delete_checked, name='delete_checked'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('check/<list_id>', views.check, name='check'),
    path('uncheck/<list_id>', views.uncheck, name='uncheck'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('count_all/', views.count_all, name='count_all'),


]
