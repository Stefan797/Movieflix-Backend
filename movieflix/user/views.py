#from django.shortcuts import render
#from django.contrib.auth.models import User
from rest_framework import viewsets, status
from .models import CustomUser
from django.core import serializers
from django.http import HttpResponse
from .serializers import CustomUserSerializer
from rest_framework.authentication import TokenAuthentication #
from rest_framework.authtoken.models import Token #
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .models import CustomUser
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import logout
import datetime

# Create your views here.

def logout_view(request):
    logout(request)
    # Redirect to a success page.

class CustomUserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer
    
class UserLogIn(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'user_name': user.username
        })

class SignUp(ObtainAuthToken): 
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        user = CustomUser.objects.create(
            username = request.POST.get('username'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email'),
            password = request.POST.get('password'),
            )
        now = datetime.datetime.now()
        print(serializer, now)
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.get(user=user)
            subject = 'welcome to Movieflix'
            message = f'Hi {user.username}, thank you for registering in Movieflix.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail( subject, message, email_from, recipient_list, token )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

