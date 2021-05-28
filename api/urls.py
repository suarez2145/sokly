from django.urls import include, path 
from rest_framework import routers
from . import views
from .views import PlayerPhotoViewSet

router = routers.DefaultRouter()
router.register(r'player', views.PlayerViewSet)
router.register(r'photos', views.PlayerPhotoViewSet,basename="photos")


urlpatterns = [
    ## this was '' but that was when my other route in sokly app was set to '' also
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]



