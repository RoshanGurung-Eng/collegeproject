from django.db import models

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




