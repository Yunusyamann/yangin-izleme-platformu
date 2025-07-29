# fires/models.py
from django.db import models

class FirePoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    bright_ti4 = models.FloatField()
    acq_date = models.DateField()
    acq_time = models.CharField(max_length=10)
    confidence = models.CharField(max_length=10)
    frp = models.FloatField()
    daynight = models.CharField(max_length=1)

    def __str__(self):
        return f"Yangın - {self.acq_date} ({self.latitude}, {self.longitude})"
