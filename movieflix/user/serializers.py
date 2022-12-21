from django.contrib.auth.models import User
from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    ##Feierabend