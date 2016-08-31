from django.conf.urls import url
from views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^index/',index),
    url(r'^folders/$',get_all_folders),
    url(r'^videos/$',get_all_videos),
    url(r'^children/([a-z]+)/([0-9]+)/$',get_children)
]

urlpatterns = format_suffix_patterns(urlpatterns)
