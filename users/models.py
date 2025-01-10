from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) 
    phone_number = models.CharField(max_length=255,unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=255,default=2)#0<=admin 1<=user 2<=driver
    profile_picture = models.ImageField(upload_to='',blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
  

    def __str__(self):
        return f"{self.username} - {self.email}"

