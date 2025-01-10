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

class VehicleOrdersCreateView(generics.ListCreateAPIView):
    queryset = VehicleOrders.objects.all()
    serializer_class = VehicleOrdersSerializer

class VehicleOrdersGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleOrders.objects.all()
    serializer_class = VehicleOrdersSerializer

class VehicleOrdersCreateView(generics.ListCreateAPIView):
    queryset = VehicleOrders.objects.all()
    serializer_class = VehicleOrdersSerializer

    def perform_create(self, serializer):
        # Get the vehicle by its ID (assuming it's passed in the request data)
        vehicle_id = self.request.data.get('vehicle')  # Get the vehicle ID
        vehicle = Vehicle.objects.get(id=vehicle_id)   # Retrieve the vehicle instance

        # Ensure the user is authenticated and retrieve the user instance
        user = self.request.user  # Get the user from the request (or handle user logic if needed)

        # Pass the vehicle and user to the serializer
        serializer.save(vehicle=vehicle, user=user)

       

