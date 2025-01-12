from django.contrib import admin
from .models import *
# Register your models here.

class VehicleCategoryDetails(admin.ModelAdmin):
    list_display = ['id', 'vehicle_name', 'category_img', 'created_at']
    search_fields = ['vehicle_name']

class VehicleDetails(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'product_img', 'price', 'created_at']
    search_fields = ['title', 'price']
    list_filter = ['created_at']

class VehicleOrdersAdmin(admin.ModelAdmin):
    list_display =  ['vehicle', 'vehicle_type', 'quantity', 'user']
    search_fields = ['id','vehicle_type','vehicle']

admin.site.register(VehicleCategory, VehicleCategoryDetails)
admin.site.register(Vehicle, VehicleDetails)
admin.site.register(VehicleOrders,VehicleOrdersAdmin )

