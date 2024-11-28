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

    def get_product(self, obj):
        vehicle = Vehicle.objects.filter(category=obj)
        return VehicleSerialization(vehicle, many=True).data


