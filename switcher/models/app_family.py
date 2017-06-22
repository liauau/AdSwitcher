from django.db import models


class Member(models.Model):
    pkg_name = models.CharField(max_length=255, primary_key=True)
    image_url = models.TextField()
    icon_url = models.TextField()
    app_name = models.CharField(max_length=255)
    latest_version = models.IntegerField()
    desc = models.CharField(max_length=255)
    install_action = models.CharField(max_length=255)
    open_action = models.CharField(max_length=255)
    public = models.BooleanField(default=True)

    def __str__(self):
        return "pkg_name: %s" % self.pkg_name + ", app_name: %s" % self.app_name \
               + ", install_action: %s" % self.install_action
