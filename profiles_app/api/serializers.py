from django.db import models
from django.db.models.base import Model
from rest_framework import serializers
from profiles_app import models

class UserProfileSerializer(serializers.ModelSerializer):
    "serializer user profile"
    
    class meta : 
        
        model = models.UserProfile
        Fields = '__all__'
        extra_kwargs = {
            'password': {"write_only":True , 
                         "style" : {
                             "input_type" : 'password'
                         }
                
            }
        }
        


def create_serializer(self,validated_data):
    
    
    user = models.UserProfile.objects.create_user(email = validated_data['email'], name = validated_data['name'], password = validated_data['password'])
    return user
    