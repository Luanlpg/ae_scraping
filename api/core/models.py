from django.db import models
from django.utils import timezone

class LogModel(models.Model):
    """=========================================================================
    Model de Log.
    ========================================================================="""
    url = models.URLField(max_length=500)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now)
