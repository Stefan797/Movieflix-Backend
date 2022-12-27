from django.contrib.auth.models import User
from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    queryset=CustomUser.objects.all()

    class Meta:
        model = CustomUser
        fields = '__all__' 