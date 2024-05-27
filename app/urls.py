# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('seller/properties/', views.seller_property_list, name='seller_property_list'),
    path('seller/add-property/', views.add_property, name='add_property'),
    path('properties/', views.property_list, name='property_list'),
    path('property/<int:property_id>/interested/', views.interested_property, name='interested_property'),
    path('property/<int:property_id>/like/', views.like_property, name='like_property'),
]
