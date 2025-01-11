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
    
from rest_framework import serializers
from .models import VehicleOrders
from users.utils import create_user

class VehicleOrdersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=False)  # Optional password field

    class Meta:
        model = VehicleOrders
        fields = '__all__'  # Do not include 'password' in fields for this serializer

    def validate(self, data):
        if not data.get('username') or not data.get('email'):
            raise serializers.ValidationError("Username and email are required to place an order.")
        return data

    def create(self, validated_data):
        # Extract the username, email, and password
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password', 'default_password')  # Use default password if not provided
        
        # Create the user using the utility function
        user = create_user(username=username, email=email, password=password)
        
        # Remove username, email, and password from the data, as they're not part of VehicleOrders model
        validated_data.pop('username', None)
        validated_data.pop('email', None)
        validated_data.pop('password', None)

        # Create the VehicleOrder and associate the user with it
        validated_data['user'] = user
        return super().create(validated_data)
