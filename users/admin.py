from django.contrib import admin
from .models import *
# Register your models here.
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['username','email', 'phone_number','profile_picture']

admin.site.register(UserDetails, UserDetailsAdmin)

