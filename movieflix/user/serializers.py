#from django.contrib.auth.models import User | kann wahrscheinlich weg
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    queryset=CustomUser.objects.all()

    class Meta:
        model = CustomUser
        fields = '__all__' 