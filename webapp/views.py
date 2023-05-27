from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import blog,User,Tag
from .serializers import blogSerializer,UserSerializer,TagSerializer

# Create your views here.
class UserList(APIView):

    def get(self,request):
        User1 = User.objects.all()
        serializer1=UserSerializer(User1, many=True) 
        return Response(serializer1.data)

    def post(self):
        pass    