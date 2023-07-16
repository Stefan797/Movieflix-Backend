import ffmpeg
from django.shortcuts import render, redirect
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings
from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer
from wsgiref.util import FileWrapper
from django.http import HttpResponse

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

def upload_movie(request):
    if request.method == 'POST':
        movie_file = request.FILES['video']
        movie = Movie.objects.create(movie_file=movie_file)

        # Pfad zum hochgeladenen Video
        movie_path = movie.movie_file.path

        # Pfad für den Screenshot
        screenshot_path = f'screenshots/{movie.pk}.jpg'

        # Screenshot erstellen
        ffmpeg.input(movie_path).filter('thumbnail', t='10').output(screenshot_path, vframes=1)
        movie.screenshot = screenshot_path
        movie.save()

        return redirect('movie_detail', pk=movie.pk)

    return render(request, 'upload_video.html')

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'video_detail.html', {'video': movie})