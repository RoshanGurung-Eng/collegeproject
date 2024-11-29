from django.urls import path
from .views import *

urlpatterns = [
    #for Customer
    path("customer",CutomerGetView.as_view(), name="customer"),
    path("create/customer",CustomerCreateView.as_view(), name="customer"),
    path("delete/customer/<int:id>",CustomerDestroyView.as_view(), name="customer"),
    #for Ordering Vehicle
    path("car-orders", CarOrdersCreateView.as_view(), name="car-orders-create"),  
    path("car-orders/<int:pk>", CarOrdersGetView.as_view(), name="car-orders-detail"),
    #for Payment
    path("esewa/callback",EsewaCallBackView.as_view(), name="esewa-callback"),
    path("esewa/payment",EsewaPaymentView.as_view(), name="esewa-Payment"),
]
