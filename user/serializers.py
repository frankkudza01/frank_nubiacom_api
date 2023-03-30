from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# serializer for new user
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password','email','first_name','last_name','user_type')

    def create(self,validate_data):
        user=User.objects.create_user(validate_data['username'],email=validate_data['email'],password=validate_data['password'],first_name=validate_data['first_name'],last_name=validate_data['last_name'])
        return user