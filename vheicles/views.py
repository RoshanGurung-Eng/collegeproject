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

