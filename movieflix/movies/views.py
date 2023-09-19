#import ffmpeg
import subprocess
# from django.shortcuts import render, redirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
#from django.views.decorators.cache import cache_page 
from django.conf import settings
from rest_framework import viewsets, status # permissions,
from .models import Movie
from .serializers import MovieSerializer
# from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import os
from rest_framework.decorators import action # api_view, permission_classes
from django.db.models import Q

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Start Get Movies Endpoints

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().order_by('-id')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    #http_method_names = ['get'] # Automatisch nur get erlaubt in der kompletten View?

    @action(methods=['GET'], detail=True)
    def get_queryset(self):
        http_method_names = ['get']
        category = self.request.query_params.get('category')
        special_category_mylist = self.request.query_params.get('special_category_mylist')
        currentuser = self.request.user
        
        if category is not None:
            self.queryset = Movie.objects.filter(category=category)

        if special_category_mylist is not None:
            self.queryset = currentuser.favorite_movies
            print('z37', self.queryset)
        return self.queryset

    def increase_likes(self, request, pk=None):
        movie = self.get_object()
        currentuser = request.user
        if not currentuser.liked_movies.filter(pk=movie.pk).exists():
            currentuser.liked_movies.add(movie)
            movie.likes += 1
            movie.save()
            response_data = {'movieLikes': movie.likes}
            print(currentuser.liked_movies)
        else: 
            currentuser.liked_movies.remove(movie)
            movie.likes -= 1
            movie.save()
            response_data = {'movieLikes': movie.likes}
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    def change_category_to_mylist(self, request, pk=None):
        movie = self.get_object()
        currentuser = request.user
        if not currentuser.favorite_movies.filter(pk=movie.pk).exists():
            currentuser.favorite_movies.add(movie)
            response_data = {'movie_myList_response': 'Title wurde erfolgreich zu ihrer Liste hinzugefügt!'}
            print(currentuser.liked_movies)
        else: 
            currentuser.favorite_movies.remove(movie)
            response_data = {'movie_myList_response': 'Title wurde aus ihrer Liste entfernt!'}

        return Response(response_data, status=status.HTTP_200_OK)
    
    def search_movies(self, request):
        search_terms = request.query_params.get('search_terms')
        title = request.query_params.get('title')
        category = request.query_params.get('category')

        queryset = Movie.objects.all()

        if search_terms:
            queryset = queryset.filter(Q(search_terms__icontains=search_terms))

        if title:
            queryset = queryset.filter(Q(title__icontains=title))

        if category:
            queryset = queryset.filter(Q(category=category))

        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)
    

# Start Upload Movies

@csrf_exempt
def upload_movie(request):
    if request.method == 'POST':
        movie_request = request.FILES['movie']
        movie = Movie.objects.create(movie_file=movie_request)

        movie_name = request.POST['title']
        movie.title = movie_name

        # Create the "screenshots" directory if it doesn't exist
        screenshot_dir = os.path.join('media/screenshots')
        #os.makedirs(screenshot_dir, exist_ok=True)

        # Generate a valid screenshot filename with a number pattern
        screenshot_filename = os.path.splitext(os.path.basename(movie.movie_file.name))[0] + '_%d.png'
        screenshot_path = os.path.join(screenshot_dir, screenshot_filename)

        # Path to the uploaded video
        movie_path = movie.movie_file.path

        # Create the screenshot
        try:
            subprocess.run(['ffmpeg', '-i', movie_path, '-vf', 'thumbnail', '-vframes', '1', screenshot_path], check=True)
            movie.screenshot = screenshot_filename  # Save the screenshot filename in the database
            movie.save()
            return HttpResponse({'moviefile': movie.movie_file})
        except subprocess.CalledProcessError as e:
            return HttpResponse(f'Fehler bei der Erstellung des Screenshots: {e.stderr}')