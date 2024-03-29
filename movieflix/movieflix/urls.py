from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from notifications.views import NotificationItemView
from user.views import CustomUserViewSet, SignUp, CreateTokenView, logout_view, activate_user
from movies.views import MovieViewSet, upload_movie
from django.views.generic.base import RedirectView


router = routers.DefaultRouter()
router.register(r'userAPI', CustomUserViewSet)
router.register(r'movieAPI', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    path('notifications/', NotificationItemView.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('movie/<int:pk>/change-category/', MovieViewSet.as_view({'get': 'change_category_to_mylist'}), name='change-category-to-mylist'),
    path('movie/<int:pk>/increase_likes/', MovieViewSet.as_view({'get': 'increase_likes'}), name='increase-likes'),
    path('upload_movie/',  upload_movie),
    path('activate/<int:user_id>/', activate_user, name='activate_user'),
    path('api/', include(router.urls)),
    path('api-user-login/', CreateTokenView.as_view(), name="token"),
    path('sign-up/', SignUp.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
    path('logout/', logout_view),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)