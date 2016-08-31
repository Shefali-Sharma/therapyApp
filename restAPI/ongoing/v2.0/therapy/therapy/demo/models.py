from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=False,max_length=10)
    manager_id = models.ForeignKey("self",default=0)

    def __str__(self):
        return self.name
