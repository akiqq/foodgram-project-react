from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]
