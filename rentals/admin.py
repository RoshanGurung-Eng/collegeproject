from django.contrib import admin
from.models import *
# Register your models here.
class CustomerDetails(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','message']
class PaymentMethod(admin.ModelAdmin):
    list_display = ['esewa_order_id','amount','status']

admin.site.register(Customer,CustomerDetails)
admin.site.register(esewaPayment, PaymentMethod)

