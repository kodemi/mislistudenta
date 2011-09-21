from django.conf.urls.defaults import patterns, url
from main.views import *

urlpatterns = patterns('',
    url(r'^$', home)
)
  