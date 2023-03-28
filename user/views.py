from django.shortcuts import render
from user.serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView


class RegisterApi(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class LoginApi(APIView):
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please put username & password'}, status=status.HTTP_400_BAD_REQUEST)
        
        user=authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token':token.key}, status=status.HTTP_200_OK)

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        

