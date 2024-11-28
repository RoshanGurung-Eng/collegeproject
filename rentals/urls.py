from django.urls import path
from .views import *

urlpatterns = [
    path("customer",CutomerGetView.as_view(), name="customer"),
    path("create/customer",CustomerCreateView.as_view(), name="customer"),
    path("delete/customer/<int:id>",CustomerDestroyView.as_view(), name="customer"),

    #esewa
    path("esewa/callback",EsewaCallBackView.as_view(), name="esewa-callback"),
    path("esewa/payment",EsewaPaymentView.as_view(), name="esewa-Payment"),
]
