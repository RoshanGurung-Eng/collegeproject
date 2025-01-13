from django.contrib import admin
from .models import *
# Register your models here.
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['username','email', 'phone_number','profile_picture']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')

admin.site.register(UserDetails, UserDetailsAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)

