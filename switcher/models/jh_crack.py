from django.db import models

from switcher.models.constant import CONTEXT, META_DATA


class JhNode(models.Model):
    # pkg_name
    p = models.CharField(max_length=255, primary_key=True)

    # probability of use this config
    pro = models.FloatField(default=0.0)

    def __str__(self):
        return 'pkg_name: %s, probability: %.2f' % (self.p, self.pro)


class JhContext(models.Model):
    # pkg_name
    p = models.CharField(max_length=255)

    # version_name
    vn = models.CharField(max_length=255)

    # version_code
    vc = models.IntegerField(default=0)

    # label
    l = models.CharField(max_length=255)

    # signatures
    sg = models.TextField()

    jh_node = models.OneToOneField('JhNode', related_name=CONTEXT, on_delete=models.CASCADE)

    def __str__(self):
        return 'pkg_name: %s' % self.p


class JhMetaData(models.Model):
    nm = models.CharField(max_length=255)
    vl = models.CharField(max_length=255)
    c = models.ForeignKey('JhContext', related_name=META_DATA, on_delete=models.CASCADE)

    def __str__(self):
        return 'name: %s' % self.nm + ', value: %s' % self.vl
