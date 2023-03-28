from blog.models import Post
from django.shortcuts import render
from blog.serializer import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


#get all posts
class PostList(generics.ListAPIView):

    queryset=Post.objects.all()
    serializer_class=PostSerializer
    filter_backends=(DjangoFilterBackend, SearchFilter)
    search_fields=('title','description')
    

# create new post
class PostCreate(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get detailed post

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        post=self.get_object(pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)

# edit or delete data
class PostEdit(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    def put(self,request,pk):
        post=self.get_object(pk)
        serializer=PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        post=self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_DELTED)
