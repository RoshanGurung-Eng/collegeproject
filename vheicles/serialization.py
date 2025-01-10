from rest_framework import serializers
from .models import *

class VehicleCategorySerialization(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = ['id', 'vehicle_name','category_img']

class VehicleSerialization(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'title', 'description','product_img','price','rental_price','category']

class VehicleCategoryListSerialization(serializers.ModelSerializer):
    vehicle = serializers.SerializerMethodField()
    class Meta:
        model = VehicleCategory
        fields = ['id', 'vehicle_name','category_img', 'vehicle']

    def get_vehicle(self, obj):
        vehicle = Vehicle.objects.filter(category=obj)
        return VehicleSerialization(vehicle, many=True).data
    
class VehicleOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleOrders
        fields = ['name', 'address', 'phone', 'vehicle', 'vehicle_type', 'quantity', 'user', 'order_status']

    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=UserDetails.objects.all())


    

