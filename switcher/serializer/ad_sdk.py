from rest_framework import serializers

from switcher.models.constant import EXPIRES_INTERVAL_TIME, VERSION_CODE, LINK, UPDATE_TIME
from switcher.models.ad_sdk import SdkNode


class SdkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SdkNode
        fields = (VERSION_CODE, LINK, UPDATE_TIME, EXPIRES_INTERVAL_TIME)
