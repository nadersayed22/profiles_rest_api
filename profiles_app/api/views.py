from .serializers import UserProfileSerializer
from profiles_app import models
from rest_framework import viewsets

class UserProfileViewsets(viewsets.ModelViewSet):
    "Handle creating, creating and updating profiles"
    
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()