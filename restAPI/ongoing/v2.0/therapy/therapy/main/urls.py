from django.conf.urls import url
from views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^index/',index),
]

urlpatterns = format_suffix_patterns(urlpatterns)
