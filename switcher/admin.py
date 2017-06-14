from django.contrib import admin
from .models.ad_config import AppNode, Placement, Context, MetaData
from .models.app_family import Member

# Register your models here.
admin.site.register(AppNode)
admin.site.register(Placement)
admin.site.register(Context)
admin.site.register(MetaData)
admin.site.register(Member)
