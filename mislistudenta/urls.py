from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mislistudenta.views.home', name='home'),
    # url(r'^mislistudenta/', include('mislistudenta.foo.urls')),
    url(r'^googlef5450b14f01d35b8.html$', TemplateView.as_view(template_name='main/googlef5450b14f01d35b8.html')),
    url(r'^', include('main.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns