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
from rest_framework.decorators import action # api_view, permission_classes
from django.db.models import Q

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category = self.request.query_params.get('category')
        special_category_mylist = self.request.query_params.get('special_category_mylist')
        #print('z26', category)
        
        if category is not None:
            self.queryset = Movie.objects.filter(category=category)
            # print('z30', self.queryset)

        if special_category_mylist is not None:
            self.queryset = Movie.objects.filter(special_category_mylist=special_category_mylist)
            # print('z35', self.queryset)
        return self.queryset

    
    def load_movie(self, request, pk=None):
        movie = self.get_object()
        serializer = self.get_serializer(movie)
        return Response(serializer.data)
    
    # @action(detail=True, methods=['get'])
    def increase_likes(self, request, pk=None):
        movie = self.get_object()
        print(movie)
        movie.likes += 1
        movie.save()
        print(movie)
        return Response({'likes': movie.likes})
    
    # @api_view(['POST'])
    # @permission_classes([permissions.IsAuthenticated])
    def change_category_to_mylist(self, request, pk=None):
        # try:
        #     movie = Movie.objects.get(pk=pk)
        # except Movie.DoesNotExist:
        #     return Response(status=404)
        movie = self.get_object()
        movie.special_category_mylist = 'mylist'
        movie.save()
        return Response({'message': 'Category changed to mylist'})
    
    @action(detail=False, methods=['get'])
    def search_movies(self, request):
        search_terms = request.query_params.get('search_terms')
        title = request.query_params.get('title')
        category = request.query_params.get('category')

        # Start mit dem kompletten Queryset
        queryset = Movie.objects.all()

        # Wenn search_terms angegeben sind, filtere nach Suchbegriffen
        if search_terms:
            queryset = queryset.filter(Q(search_terms__icontains=search_terms))

        # Wenn title angegeben ist, filtere nach Titel
        if title:
            queryset = queryset.filter(Q(title__icontains=title))

        # Wenn category angegeben ist, filtere nach Kategorie
        if category:
            queryset = queryset.filter(Q(category=category))

        serializer = MovieSerializer(queryset, many=True)
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