from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import CustomUser
from django.core import serializers
from django.http import HttpResponse
from .serializers import CustomUserSerializer
from rest_framework.authentication import TokenAuthentication #
from rest_framework.authtoken.models import Token #
from rest_framework.permissions import IsAuthenticated  # <-- Here


# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)             # <-- And here
    authentication_classes = [TokenAuthentication]#
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer


def login(request):
    user_name = request.get('user_name')
    password = request.get('password')
    token = Token.objects.create(user=...)#
    print(token.key)#
    return



# date_joined mit aktuellem datum versehen

