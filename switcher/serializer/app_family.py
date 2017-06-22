from rest_framework import serializers
from switcher.models.app_family import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'pkg_name', 'image_url', 'icon_url', 'app_name', 'desc', 'install_action', 'open_action', 'public')
