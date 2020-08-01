import pytz
from django.db import models
from django.utils import timezone

class ActivityPeriod(models.Model):
    real_name = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    tz = models.CharField(max_length=50, choices=pytz.all_timezones)

    def __str__(self):
        return '{} {}'.format(self.real_name, self.start_time)