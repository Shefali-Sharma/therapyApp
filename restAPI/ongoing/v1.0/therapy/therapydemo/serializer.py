from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User

class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        # to restrict us sending two attributes
        #fields = ('foldername','parentid')
        # to send all
        fields = '__all__'




class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


