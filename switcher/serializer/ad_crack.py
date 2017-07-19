from rest_framework import serializers

from switcher.models.ad_crack import CrackContext, CrackNode, CrackPlacement
from ..models.ad_crack import PLACEMENT, CONTEXT, SID, EXTRA, START_TIMES, MAX_TIMES, PKG_NAME, VERSION_CODE, \
    VERSION_NAME, LABEL, SIGNATURES, EXPIRES_INTERVAL_TIME, JH_ENABLE, FB_ENABLE


class CrackPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrackPlacement
        fields = ('id', SID, EXTRA, START_TIMES, MAX_TIMES)
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class CrackContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrackContext
        fields = (PKG_NAME, VERSION_NAME, VERSION_CODE, LABEL, SIGNATURES)


class CrackNodeSerializer(serializers.ModelSerializer):
    c = CrackContextSerializer()
    pl = CrackPlacementSerializer(many=True)

    class Meta:
        model = CrackNode
        fields = (PKG_NAME, EXPIRES_INTERVAL_TIME, FB_ENABLE, JH_ENABLE, PLACEMENT, CONTEXT)

    def create(self, validated_data):
        placement_data = validated_data.pop(PLACEMENT)
        context_data = validated_data.pop(CONTEXT)

        # create node
        crack_node = CrackNode.objects.create(**validated_data)

        # create placement array
        for placement in placement_data:
            CrackPlacement.objects.create(crack_node=crack_node, **placement)

        # create context
        CrackContext.objects.create(crack_node=crack_node, **context_data)
        print(context_data)

        return crack_node

    def update(self, instance, validated_data):
        placement_data = validated_data.pop(PLACEMENT)
        context_data = validated_data.pop(CONTEXT)
        self.update_node(instance, validated_data)
        self.update_pm(crack_node=instance, placement_data=placement_data)
        self.update_context(crack_node=instance, context_data=context_data)
        return instance

    def update_node(self, node, node_data):
        node.ext = node_data.get(EXPIRES_INTERVAL_TIME, node.ext)
        node.fe = node_data.get(FB_ENABLE, node.fe)
        node.je = node_data.get(JH_ENABLE, node.je)
        node.save()
        return node

    def update_pm(self, crack_node, placement_data):
        for pm in placement_data:
            if pm:
                expected_pm_id = pm.get('id', None)
                if expected_pm_id:
                    old_pm_obj = CrackPlacement.objects.get(id=expected_pm_id, crack_node=crack_node)
                    old_pm_obj.s = pm.get(SID, old_pm_obj.s)
                    old_pm_obj.e = pm.get(EXTRA, old_pm_obj.e)
                    old_pm_obj.st = pm.get(START_TIMES, old_pm_obj.st)
                    old_pm_obj.mt = pm.get(MAX_TIMES, old_pm_obj.mt)
                    old_pm_obj.save()
                else:
                    CrackPlacement.objects.create(crack_node=crack_node, **pm)

    def update_context(self, crack_node, context_data):
        context_obj = CrackContext.objects.get(crack_node=crack_node)
        context_obj.p = context_data.get(PKG_NAME, context_obj.p)
        context_obj.vn = context_data.get(VERSION_NAME, context_obj.vn)
        context_obj.vc = context_data.get(VERSION_CODE, context_obj.vc)
        context_obj.l = context_data.get(LABEL, context_obj.l)
        context_obj.sg = context_data.get(SIGNATURES, context_obj.sg)
        context_obj.save()
