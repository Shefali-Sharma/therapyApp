from rest_framework import serializers

from .models import Folder

class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        # to restrict us sending two attributes
        #fields = ('foldername','parentid')
        # to send all
        fields = '__all__'

