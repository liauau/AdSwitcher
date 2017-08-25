from django.db import models


class SdkNode(models.Model):
    # current version code
    vc = models.IntegerField(default=0)

    # link address of download
    lk = models.CharField(max_length=255, default='')

    # update time
    ut = models.IntegerField(default=0)

    # expires time
    et = models.IntegerField(default=0)

    def __str__(self):
        return self.l
