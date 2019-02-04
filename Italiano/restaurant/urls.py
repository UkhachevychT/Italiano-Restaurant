from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('book/', views.book),
    path('menu/', views.menu),
    path('gallery/', views.gallery),
    path('booking/', views.reservation),
    path('contact/', views.contact),
    path('contact_result/', views.contact_result),
]
