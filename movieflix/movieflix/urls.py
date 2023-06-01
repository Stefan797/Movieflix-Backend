"""movieflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from user.views import CustomUserViewSet
from movies.views import MovieViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from movies.views import show_movie
from user.views import UserLogIn, SignUp, logout_view
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()
router.register(r'userAPI', CustomUserViewSet)
router.register(r'movieAPI', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
   
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('__debug__/', include('debug_toolbar.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('movieST/<str:title>/', show_movie),
    path('api-user-login/', UserLogIn.as_view()),
    path('sign-up/', SignUp.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
    path('logout/', logout_view),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

 # path('api-auth/', include('rest_framework.urls')),