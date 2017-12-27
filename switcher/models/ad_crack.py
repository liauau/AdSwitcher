from django.db import models

from switcher.models.constant import PLACEMENT, CONTEXT


class CrackNode(models.Model):
    # pkg_name
    p = models.CharField(max_length=255, primary_key=True)

    # ad enable switch
    ae = models.BooleanField(default=True)

    # fb ad enable switch
    fe = models.BooleanField(default=True)

    # jh ad enable switch
    je = models.BooleanField(default=True)

    # outer ad enable switch
    oe = models.BooleanField(default=True)

    # expires time in seconds, default value is 24 * 60 * 60s, 1 day
    et = models.IntegerField(default=86400)

    # interval of interstitial ad show
    ii = models.IntegerField(default=600)

    # click strategy
    cs = models.IntegerField(default=0)

    # the interval of interstitial ad clicked to be action after shown, the unit is millisecond
    cd = models.IntegerField(default=1000)

    # what ad platform using.
    # 0 = Facebook
    # 1 = AppNext
    gp = models.IntegerField(default=0)

    def __str__(self):
        return 'pkg_name: %s' % self.p


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
        return 'sid: %s' % self.s + ', extra: %s' % self.e


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
        return 'pkg_name: %s' % self.p
