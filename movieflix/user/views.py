from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import CustomUser
from django.core import serializers
from django.http import HttpResponse
from .serializers import CustomUserSerializer
# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer

#    def create(self, request):
#       if request.method == 'POST':
#            """
#            This is a view to create an CustomUser.
#            """
#            new_User = CustomUser.objects.create(
#                email=request.POST['email'], 
#                first_name=request.POST['first_name'], 
#                last_name=request.POST['last_name'],
#                password=request.POST['password'])
#            new_User.save()

           # serzialized_customUser = serializers.serialize('json', [new_User, ])
         #   return HttpResponse(serzialized_customUser, content_type='application/json')


# date_joined mit aktuellem datum versehen