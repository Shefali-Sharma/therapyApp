from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^index/',index),
    url(r'^demoview/$',DemoView.as_view()),
    url(r'^modifieddemoview/$',ModifiedDemoView.as_view()),
    url(r'^demojson/$',demojsonresponse),
    url(r'^employees/$',employees),
]