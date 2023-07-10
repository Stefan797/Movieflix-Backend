from rest_framework import viewsets, status
from .models import CustomUser
# from django.core import serializers
from django.http import HttpResponse
from .serializers import CustomUserSerializer
# from rest_framework.authentication import TokenAuthentication 
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated  
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .models import CustomUser
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import logout
# import datetime
from .serializers import AuthTokenSerializer
from rest_framework.settings import api_settings
from django.contrib.auth.hashers import make_password

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponse(status=204)
    # Redirect to a success page.

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer
    

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    # 

    # def post(self, request, *args, **kwargs):
    #     """
    #     To login a new user, we need to validate request data, 
    #     if not valid return bad request, else create user from valid request data, 
    #     send registration successful email to new user and response created.
    #     """
    #     serializer = CustomUserSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #     user = create_user_from_request_data(request.data)
    #     # send_register_mail_to_newuser(user)
    #     response_data = {
    #         'username': user.username,
    #         'email': user.email,
    #         'message': 'You registered successfully.',
    #     }
    #     return Response(response_data, status=status.HTTP_201_CREATED)


class SignUp(ObtainAuthToken): 
    def post(self, request, *args, **kwargs):
        """
        To register a new user, we need to validate request data, 
        if not valid return bad request, else create user from valid request data, 
        send registration successful email to new user and response created.
        """
        serializer = CustomUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = create_user_from_request_data(request.data)
        # send_register_mail_to_newuser(user)
        response_data = {
            'username': user.username,
            'email': user.email,
            'message': 'You registered successfully.',
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

def create_user_from_request_data(request_data):
    password = request_data.get('password')
    hashed_password = make_password(password)

    user = CustomUser.objects.create(
        username=request_data.get('username'),
        first_name=request_data.get('first_name'),
        last_name=request_data.get('last_name'),
        email=request_data.get('email'),
        password=hashed_password,
    )
    return user


# def send_register_mail_to_newuser(user):
#     """
#     Sends a email to the given user.
    
#     Parameters
#     ----------
#     user : CustomUser
#         The user to send email to.
#     """
#     subject = 'welcome to Movieflix'
#     message = f'Hi {user.username}, thank you for registering in Movieflix.'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [user.email]

#     To do after confirm make is active true in database!!!
#     send_mail( subject, message, email_from, recipient_list )