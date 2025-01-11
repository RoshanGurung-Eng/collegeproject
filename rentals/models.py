from django.db import models
from vheicles.models import *

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name and self.last_name
    
class esewaPayment(models.Model):
    esewa_order_id = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    order = models.ForeignKey(VehicleOrders, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255, choices=[
        ('Pending', 'Pending'), ('Success', 'Success'), ('Failed', 'Failed')], 
        default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.esewa_order_id