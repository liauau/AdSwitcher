from switcher.models.ad_crack import CrackContext, CrackNode, CrackPlacement
from rest_framework import serializers


class CrackPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrackPlacement
        fields = ('id', 'sid', 'extra')
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class CrackContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrackContext
        fields = ('platform', 'pkg_name', 'version_name', 'version_code',
                  'label', 'signatures', 'extra')


class CrackNodeSerializer(serializers.ModelSerializer):
    context = CrackContextSerializer()
    placements = CrackPlacementSerializer(many=True)

    class Meta:
        model = CrackNode
        fields = ('pkg_name', 'placements', 'context')

    def create(self, validated_data):
        placement_data = validated_data.pop('placements')
        context_data = validated_data.pop('context')

        crack_node = CrackNode.objects.create(**validated_data)
        for placement in placement_data:
            CrackPlacement.objects.create(crack_node=crack_node, **placement)
        CrackContext.objects.create(crack_node=crack_node, **context_data)
        print(context_data)
        return crack_node

    def update(self, instance, validated_data):
        placement_data = validated_data.pop('placements')
        context_data = validated_data.pop('context')
        self.update_pm(crack_node=instance, placement_data=placement_data)
        self.update_context(crack_node=instance, context_data=context_data)
        return instance

    def update_pm(self, crack_node, placement_data):
        for pm in placement_data:
            if pm:
                expected_pm_id = pm.get('id', None)
                if expected_pm_id:
                    old_pm_obj = CrackPlacement.objects.get(id=expected_pm_id, crack_node=crack_node)
                    old_pm_obj.sid = pm.get('sid', old_pm_obj.sid)
                    old_pm_obj.extra = pm.get('extra', old_pm_obj.extra)
                    old_pm_obj.save()
                else:
                    CrackPlacement.objects.create(crack_node=crack_node, **pm)

    def update_context(self, crack_node, context_data):
        context_obj = CrackContext.objects.get(crack_node=crack_node)
        context_obj.platform = context_data.get('platform', context_obj.platform)
        context_obj.pkg_name = context_data.get('pkg_name', context_obj.pkg_name)
        context_obj.version_name = context_data.get('version_name', context_obj.version_name)
        context_obj.version_code = context_data.get('version_code', context_obj.version_code)
        context_obj.label = context_data.get('label', context_obj.label)
        context_obj.signatures = context_data.get('signatures', context_obj.signatures)
        context_obj.extra = context_data.get('extra', context_obj.extra)
        context_obj.save()
