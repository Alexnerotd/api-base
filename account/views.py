from django.shortcuts import render

from user.models import MyUser

from .serializers import MyUserSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.

class Admin(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()

    
