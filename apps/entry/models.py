from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_level = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)