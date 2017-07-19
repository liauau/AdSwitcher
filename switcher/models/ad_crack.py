from django.db import models

EXPIRES_INTERVAL_TIME = 'ext'
FB_ENABLE = 'fe'
JH_ENABLE = 'je'

PLACEMENT = 'pl'
CONTEXT = 'c'

SID = 's'
PKG_NAME = 'p'
EXTRA = 'e'
START_TIMES = 'st'
MAX_TIMES = 'mt'
VERSION_NAME = 'vn'
VERSION_CODE = 'vc'
LABEL = 'l'
SIGNATURES = 'sg'


class CrackNode(models.Model):
    # pkg_name
    p = models.CharField(max_length=255, primary_key=True)

    # expires time in seconds, default value is 24 * 60 * 60s, 1 day
    ext = models.IntegerField(default=86400)

    # fb ad enable switch
    fe = models.BooleanField(default=True)

    # jh ad enable switch
    je = models.BooleanField(default=True)

    def __str__(self):
        return 'pkg_name: %s' % self.pkg_name


class CrackPlacement(models.Model):
    # sid
    s = models.IntegerField(default=0)

    # start_times
    st = models.IntegerField(default=0)

    # max_times
    mt = models.IntegerField(default=0)

    # extra(fbId)
    e = models.TextField(default='', blank=True, null=True)

    crack_node = models.ForeignKey('CrackNode', related_name=PLACEMENT, on_delete=models.CASCADE)

    def __str__(self):
        return 'sid: %s' % self.sid + ', extra: %s' % self.extra


class CrackContext(models.Model):
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

    crack_node = models.OneToOneField('CrackNode', related_name=CONTEXT, on_delete=models.CASCADE)

    def __str__(self):
        return 'pkg_name: %s' % self.pkg_name
