from django.shortcuts import render
from django.http import Http404


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import MyUser
from .serializers import *

# Create your views here.


class Register(APIView):

    def get(self, format = None):

        format = {
            "username":"data(required)",
            "email":"data(required)",
            "password":"data(required)",
            "name":"data(required)",
        }
        return Response(format, status=status.HTTP_200_OK)


    def post(self, request, format = None):
        user_serializer = MyUserSerializerPOST(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"Los datos ingresados no son validos"}, status=status.HTTP_400_BAD_REQUEST)
        

class GETPUTUserView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, format = None):
        user = MyUser.objects.get(pk=request.user.pk)
        user_serializer = MyUserSerializerGET(user)

        if user.is_authenticated:
            return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, format = None):
        user = MyUser.objects.get(pk=request.user.pk)
        user_serializer = MyUserSerializerPUT(user, data=request.data, partial = True)

        if user.is_authenticated:
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error":"Los datos ingresados no son validos."})
        else:
            return Response({"Unauthorized":"No tienes authorizacion para realizar esta accion"}, status=status.HTTP_401_UNAUTHORIZED)
        

class Logout(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, format = None):
        user = MyUser.objects.get(pk = request.user.pk)
        user_serializer = MyUserSerializerDELETE(user)

        if user.is_authenticated:
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, format = None):
        user = MyUser.objects.get(pk = request.user.pk)
        if user.is_authenticated:
            user.delete()
            return Response({"message":"Not found"}, status=status.HTTP_404_NOT_FOUND)