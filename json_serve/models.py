import pytz
from django.db import models
from django.utils import timezone

class ActivityPeriod(models.Model):
    real_name = models.TextField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    tz = models.CharField(max_length=50, choices=TIMEZONES)

    def __str__(self):
        return '{} {}'.format(self.real_name, self.start_time)