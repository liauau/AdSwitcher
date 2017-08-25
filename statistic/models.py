from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import models


class Stat(models.Model):
    user_id = models.CharField(max_length=255)
    android_id = models.CharField(max_length=255)
    google_ad_id = models.CharField(max_length=255)
    referer = models.CharField(max_length=255)
    time_offset = models.IntegerField(default=0)
    locale = models.CharField(max_length=255)

    def __str__(self):
        return 'user_id: %s' % self.user_id + ', google_id: %s' % self.google_ad_id


class Event(models.Model):
    name = models.CharField(max_length=255)
    log_time = models.IntegerField(default=0)
    params = JSONField()
    stat = models.ForeignKey('Stat', related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return 'name: %s' % self.name + ', log_time: %s' + self.log_time.value_to_string()


class EventInfo(object):
    name = ""
    count = 0
    user_count = 0
