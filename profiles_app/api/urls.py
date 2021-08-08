
from .views import UserProfileViewsets
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', UserProfileViewsets )

urlpatterns = [
    path('', include(router.urls))
]