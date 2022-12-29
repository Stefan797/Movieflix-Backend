from django.contrib.auth.models import User
from .models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    queryset = Movie.objects.all()

    class Meta:
        model = Movie
        fields = '__all__' 