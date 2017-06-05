from __future__ import unicode_literals

from django.db import models


class AppNode(models.Model):
    pkg_name = models.CharField(max_length=255, unique=True, primary_key=True)
    owner = models.ForeignKey('auth.user', related_name='switcher', on_delete=models.CASCADE)

    def __str__(self):
        return 'pkg: %s' % self.pkg_name + ', owner: %s' % self.owner


class Placement(models.Model):
    platform = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sid = models.IntegerField()
    extra = models.TextField()
    shadow = models.BooleanField()
    app = models.ForeignKey('AppNode', related_name='placements', on_delete=models.CASCADE)

    def __str__(self):
        return 'name: %s' % self.name + ', platform: %s' % self.platform


class Context(models.Model):
    platform = models.CharField(max_length=255)
    pkg_name = models.CharField(max_length=255)
    version_name = models.CharField(max_length=255)
    version_code = models.IntegerField()
    label = models.CharField(max_length=255)
    signatures = models.TextField()
    app = models.ForeignKey('AppNode', related_name='context', on_delete=models.CASCADE)

    def __str__(self):
        return 'pkg_name: %s' % self.pkg_name


class MetaData(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    context = models.ForeignKey('Context', related_name='meta_data', on_delete=models.CASCADE)

    def __str__(self):
        return 'name: %s' % self.name + ', value: ' % self.value
