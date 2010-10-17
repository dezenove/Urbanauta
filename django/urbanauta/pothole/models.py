# -*- coding: utf-8 -*-

from django.contrib.gis.db import models

class Pothole(models.Model):
    point = models.PointField()
    description = models.TextField(blank=True, null=True, verbose_name=u'Descrição')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Overriding the default manager with a GeoManager instance
    # This is required to perform spatial queries
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s' % (self.point.x, self.point.y)