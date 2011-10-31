from django.conf.urls.defaults import patterns, url
from django.views.generic.base import TemplateView
from main.views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^order', order),
    url(r'^subscribe/(?P<order_number>.*)', subscribe),
    url(r'^contacts', contacts, name='contacts'),
    url(r'^more', TemplateView.as_view(template_name='main/more.html'), name='more'),
)
  