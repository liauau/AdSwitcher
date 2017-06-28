from django.db import models


class CrackNode(models.Model):
    pkg_name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return 'pkg_name: %s' % self.pkg_name


class CrackPlacement(models.Model):
    sid = models.IntegerField(default=0)
    extra = models.TextField(default='', blank=True, null=True)
    crack_node = models.ForeignKey('CrackNode', related_name='placements', on_delete=models.CASCADE)

    def __str__(self):
        return 'sid: %s' % self.sid + ', extra: %s' % self.extra


class CrackContext(models.Model):
    pkg_name = models.CharField(max_length=255)
    version_name = models.CharField(max_length=255)
    version_code = models.IntegerField(default=0)
    label = models.CharField(max_length=255)
    signatures = models.TextField()
    crack_node = models.OneToOneField('CrackNode', related_name='context', on_delete=models.CASCADE)

    def __str__(self):
        return 'pkg_name: %s' % self.pkg_name
