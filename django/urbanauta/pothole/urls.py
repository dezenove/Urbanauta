from django.conf.urls.defaults import *

urlpatterns = patterns('pothole.views',
    (r'^add$', 'add'),
    (r'^kml$', 'kml'),
    (r'^json$', 'json'),
    (r'^geojson$', 'geojson'),
    (r'^$', 'index'),
)