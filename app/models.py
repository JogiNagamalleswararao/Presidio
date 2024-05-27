# models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    is_seller = models.BooleanField(default=False)

class Property(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='properties')
    place = models.CharField(max_length=100)
    area = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    hospitals_nearby = models.TextField(blank=True, null=True)
    colleges_nearby = models.TextField(blank=True, null=True)

class InterestedBuyer(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='interested_properties')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

class PropertyLike(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='liked_properties')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)