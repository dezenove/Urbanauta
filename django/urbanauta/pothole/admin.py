# -*- coding: utf-8 -*-

from django.contrib.gis import admin
from models import Pothole

admin.site.register(Pothole, admin.GeoModelAdmin)