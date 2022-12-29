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
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer


class UserLogIn(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['CustomUserSerializer']
        token = Token.objects.get(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'user_name': user.user_name
        })

""" 

def login(request):
    user_name = request.get('user_name')
    password = request.get('password')
    token = Token.objects.create(user=...)#
    print(token.key)#
    return """



# date_joined mit aktuellem datum versehen

