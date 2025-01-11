from django.shortcuts import render
from rest_framework import generics, viewsets
from .serialization import *
from .models import *
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class VehicleCategoryView(viewsets.ViewSet):
    def list(self, request):
        queryset = VehicleCategory.objects.all()
        serializer = VehicleCategorySerialization(queryset, many =True)
        return Response(serializer.data)
    
class VehicleCategoryCreateView(generics.CreateAPIView):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerialization

class VehicleCategoryGetbyidView(generics.RetrieveAPIView):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategoryListSerialization
    lookup_field ='id'

class VehicleView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerialization
    pagination_class = PageNumberPagination 
    permission_classes = [permissions.AllowAny]

class VehicleAddView(generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerialization
    permission_classes = [permissions.IsAuthenticated]

class VehicleGetbyidView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerialization
    def get_object(self):
        try:
            return super().get_object()
        except Vehicle.DoesNotExist:
            raise NotFound(detail="Vehicle not found", code=404)


class VehicleUpdateView(generics.UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerialization

class VehicleDeleteView(generics.DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerialization
    permission_classes = [permissions.IsAuthenticated]

class SearchView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerialization
    pagination_class = PageNumberPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            search_query = self.request.query_params.get('title', None)

            if search_query:
                queryset = queryset.filter(title__icontains=search_query)

            return queryset
        except Exception as e:
            return Response({"error": "No Product Found"}, status=400)

class VehicleOrdersGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleOrders.objects.all()
    serializer_class = VehicleOrdersSerializer

from users.utils import create_user
from rest_framework.exceptions import ValidationError


class VehicleOrdersCreateView(generics.ListCreateAPIView):
    queryset = VehicleOrders.objects.all()
    serializer_class = VehicleOrdersSerializer

    def perform_create(self, serializer):
        # Get the data from the request
        username = self.request.data.get('username')
        email = self.request.data.get('email')
        password = self.request.data.get('password', 'default_password')  # Default password if none provided

        # Ensure that username and email are present in the request
        if not username:
            raise ValidationError("Username is required.")
        if not email:
            raise ValidationError("Email is required.")
        
        # Create the user with the given username, email, and password
        user = create_user(username=username, email=email, password=password)

        # Get the vehicle ID and ensure the vehicle exists
        vehicle_id = self.request.data.get('vehicle')
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
        except Vehicle.DoesNotExist:
            raise ValidationError("Vehicle not found.")

        # Save the order with the associated user and vehicle
        serializer.save(vehicle=vehicle, user=user)