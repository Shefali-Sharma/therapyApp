from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import *
from .models import *
from .serializer import *
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User


#List All Folder or create a new one
# folder/
class FolderList(APIView):

    def get(self, request):
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class VideoList(APIView):

    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class GetChildren():
    pass


def index(request):
    return HttpResponse("Hello")


