import ffmpeg
import subprocess
# from django.shortcuts import render, redirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings
from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import os

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        
        category = self.request.query_params.get('category')
        if category is not None:
            self.queryset = Movie.objects.filter(category=category)
        return self.queryset
    
    def load_movie(self, request, pk=None):
        movie = self.get_object()
        serializer = self.get_serializer(movie)
        return Response(serializer.data)

@cache_page(CACHE_TTL)
def show_movie(request, title):
    if request.method == "GET":
        movie = Movie.objects.get(title=title)
        test = movie.movie_file.path
        print(test)
        file = FileWrapper(open(test, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        dynamic_response = 'attachment; filename=' + test
        response['Content-Disposition'] = dynamic_response
    return response


@csrf_exempt
def upload_movie(request):
    if request.method == 'POST':
        movie_request = request.FILES['movie']
        movie = Movie.objects.create(movie_file=movie_request)

        movie_name = request.POST['title']
        movie.title = movie_name

        # Create the "screenshots" directory if it doesn't exist
        screenshot_dir = os.path.join('screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)

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