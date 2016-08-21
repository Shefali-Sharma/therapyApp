from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Folder
from .serializer import FolderSerializer
from django.http import HttpResponse


#List All Folder or create a new one
# folder/
class FolderList(APIView):

    def get(self, request):
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

    def post(self):
        pass





def index(request):
    return HttpResponse("Hello")



