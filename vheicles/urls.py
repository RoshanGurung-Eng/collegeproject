from django.urls import path
from .views import *

urlpatterns = [
    #For Vehicle Categoris
    path("categories", VehicleCategoryView.as_view({'get': 'list'}), name="list-categories"),
    path("categories/add", VehicleCategoryCreateView.as_view(), name="add-category"),
    path("categories/<int:id>", VehicleCategoryGetbyidView.as_view(), name="get-category"),
    #For Vehicles
    path("vehicles", VehicleView.as_view(), name="list-vehicles"),
    path("vehicles/add", VehicleAddView.as_view(), name="add-vehicle"),
    path("vehicles/<int:pk>", VehicleGetbyidView.as_view(), name="get-vehicle"),
    path("vehicles/<int:pk>/update", VehicleUpdateView.as_view(), name="update-vehicle"),
    path("vehicles/<int:pk>/delete", VehicleDeleteView.as_view(), name="delete-vehicle"),
    #for searchgi
    path("search",SearchView.as_view(), name="search"),
     #for Ordering Vehicle
    path("Vehicle-orders", VehicleOrdersCreateView.as_view(), name="Vehicle-orders-create"),  
    path("Vehicle-orders/<int:pk>", VehicleOrdersGetView.as_view(), name="Vehicle-orders-detail"),

]
