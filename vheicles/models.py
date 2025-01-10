from django.db import models
from users.models import *

# Create your models here.
class VehicleCategory(models.Model):
    vehicle_name = models.CharField(max_length= 255)
    category_img = models.ImageField(upload_to="category/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_name

class Vehicle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(VehicleCategory, on_delete=models.SET_NULL,null=True,blank=True)
    product_img = models.ImageField(upload_to="product/", null=True, blank=True)
    price= models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class VehicleOrders(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('scooter', 'Scooter'),
    ]
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.IntegerField(default=0)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_type = models.CharField(
        max_length=255,
        choices=VEHICLE_TYPE_CHOICES,
        default='car'
    )  
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True)    
    orderStatus = models.CharField(
    max_length=255,
    choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
    ],
    default='Pending'
)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username