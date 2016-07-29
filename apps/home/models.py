from __future__ import unicode_literals
import json
from django.db import models
from ..entry.models import User
from decimal import Decimal

class MarkerIcon(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    eventDay = models.CharField(max_length=200)
    eventStart = models.CharField(max_length=200)
    eventEnd = models.CharField(max_length=200)
    requirements = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=12, decimal_places=9)
    lon = models.DecimalField(max_digits=12, decimal_places=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_json(self):
    	return dict(
    		input_id = self.id,
    		title = self.title,
            description = self.description,
            eventDay = self.eventDay,
            eventStart = self.eventStart,
            eventEnd = self.eventEnd,
            requirements = self.requirements,
    		lat = float(self.lat),
    		lon = float(self.lon),
    		created_at = self.created_at.isoformat(),
    		updated_at = self.updated_at.isoformat())
