from django.contrib import admin
from .models import *

admin.site.register(Folder)
admin.site.register(Video)
admin.site.register(Video_folder_mapping)
