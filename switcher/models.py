from __future__ import unicode_literals

from django.db import models


class AppNode(models.Model):
    pkg_name = models.CharField(max_length=255, unique=True, primary_key=True)
    owner = models.ForeignKey('auth.user', related_name='switcher', on_delete=models.CASCADE)

    def __str__(self):
        return 'pkg: %s' % self.pkg_name + ', owner: %s' % self.owner


class Mix(models.Model):
    default_platform = models.CharField(max_length=255)
    app = models.OneToOneField('AppNode', on_delete=models.CASCADE)

    def __str__(self):
        return 'default_platform: %s' % self.default_platform


class PlacementMappings(models.Model):
    platform = models.CharField(max_length=255)
    placement = models.CharField(max_length=255)
    mix = models.ForeignKey('Mix', related_name='placement_mappings', on_delete=models.CASCADE)

    def __str__(self):
        return 'platform: %s' % self.platform + ', placement: %s' % self.placement


class Context(models.Model):
    platform = models.CharField(max_length=255)
    pkg_name = models.CharField(max_length=255)
    version_name = models.CharField(max_length=255)
    version_code = models.IntegerField()
    label = models.CharField(max_length=255)
    signatures = models.CharField(max_length=255)
    app = models.ForeignKey('AppNode', related_name='context', on_delete=models.CASCADE)

    def __str__(self):
        return 'pkg_name: %s' % self.pkg_name
