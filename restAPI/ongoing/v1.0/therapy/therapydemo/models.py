from __future__ import unicode_literals

from django.db import models

class Folder(models.Model):
    folderid = models.IntegerField()
    foldername = models.CharField(max_length=20)
    parentid = models.IntegerField()

    def __str__(self):
        return self.foldername

