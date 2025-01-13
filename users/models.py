from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) 
    phone_number = models.CharField(max_length=255,unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=255,choices=[('admin', 'Admin'), ('user', 'User')], default='admin') 
    profile_picture = models.ImageField(upload_to='',blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
  

    def __str__(self):
        return f"{self.username} - {self.email}"

class ContactMessage(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=100)  
    email = models.EmailField(unique=True) 
    subject = models.CharField(max_length=200) 
    message = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.subject}"

