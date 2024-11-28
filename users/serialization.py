from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User =get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username', 'password')
        extra_kwargs = {'password':{'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)

    def update(self,instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance

class UpdateProfileSerializer(serializers.ModelSerializer):
    model = User
    fields = ('email', 'username',)

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.save()
        return instance
