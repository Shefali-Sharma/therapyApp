from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from .utilities import *

class Folder(models.Model):
    folder_id = models.IntegerField(primary_key=True,blank=False)
    folder_name = models.CharField(max_length=20, blank=False)
    parent_id = models.ForeignKey("self",null=True,blank=True)
    def __str__(self):
        return str(self.folder_id) +" "+ self.folder_name

class Video(models.Model):
    video_id = models.IntegerField(blank=False,primary_key=True)
    video_name = models.CharField(max_length=255,blank=False)
    video_path = models.CharField(max_length=255,blank=False)
    video_date_modified = models.DateTimeField(default=timezone.now())
    #video_local_path = models.CharField(max_length=45,blank=True,default=get_path(video_id))
    #models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.video_name

class Video_folder_mapping(models.Model):
    video_id = models.ForeignKey(Video)
    folder_id = models.ForeignKey(Folder)
    def __str__(self):
        tablerpr = "Video: \"" + str(self.video_id) + "\" MAPPED TO \t Parent Folder: \"" + str(self.folder_id)+ "\""
        return tablerpr