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
    
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        try:
            refresh_token = RefreshToken(self.token)
            refresh_token.blacklist()

        except Exception as e:
            self.fail('invalid_token')

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name','email', 'subject','message']
    def validate_email(self, value):
        if not value.endswith("@example.com"):  # Example custom validation
            raise serializers.ValidationError("Email must be from example.com")
        return value