from rest_framework import serializers
from .models.config import AppNode, Context, Placement, MetaData


class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ('id', 'name', 'platform', 'sid', 'extra', 'shadow')
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = ('id', 'name', 'value')
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class ContextSerializer(serializers.ModelSerializer):
    meta_data = MetaDataSerializer(many=True)

    class Meta:
        model = Context
        fields = ('id', 'platform', 'pkg_name', 'version_name', 'version_code',
                  'label', 'signatures', 'meta_data')
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class AppNodeSerializer(serializers.ModelSerializer):
    pkg_name = serializers.CharField(max_length=255)
    context = ContextSerializer(many=True)
    placements = PlacementSerializer(many=True)

    class Meta:
        model = AppNode
        fields = ('pkg_name', 'placements', 'context')

    def create(self, validated_data):
        placements_data = validated_data.pop('placements')
        context_data = validated_data.pop('context')

        app_node = AppNode.objects.create(**validated_data)

        for placement in placements_data:
            Placement.objects.create(app=app_node, **placement)

        for contextItem in context_data:
            md_data = contextItem.pop('meta_data')
            context = Context.objects.create(app=app_node, **contextItem)
            for meta_item in md_data:
                MetaData.objects.create(context=context, **meta_item)

        return app_node

    def update(self, instance, validated_data):
        placements_data = validated_data.pop('placements')
        context_data = validated_data.pop('context')

        self.update_appnode(instance, validated_data)
        self.update_pm(instance, placements_data)
        self.update_context(instance, context_data)
        return instance

    def update_appnode(self, app_node, appnode_data):
        # do not update pkg_name since it is primary key of db.
        # app_node.pkg_name = appnode_data.get('pkg_name', app_node.pkg_name)
        app_node.save()

    def update_pm(self, app_node, placements_data):
        for pm in placements_data:
            if pm:
                expected_pm_id = pm.get('id', None)
                if expected_pm_id:
                    old_pm_obj = Placement.objects.get(id=expected_pm_id, app=app_node)
                    old_pm_obj.name = pm.get('name', old_pm_obj.name)
                    old_pm_obj.platform = pm.get('platform', old_pm_obj.platform)
                    old_pm_obj.sid = pm.get('sid', old_pm_obj.sid)
                    old_pm_obj.extra = pm.get('extra', old_pm_obj.extra)
                    old_pm_obj.shadow = pm.get('shadow', old_pm_obj.shadow)
                    old_pm_obj.save()
                else:
                    Placement.objects.create(app=app_node, **pm)

    def update_context(self, app_node, context_data):
        for single_context in context_data:
            if single_context:
                expected_context_id = single_context.get('id')
                md_data = single_context.pop('meta_data')
                if expected_context_id:
                    old_context_obj = Context.objects.get(id=expected_context_id, app=app_node)
                    old_context_obj.platform = single_context.get('platform', old_context_obj.platform)
                    old_context_obj.pkg_name = single_context.get('pkg_name', old_context_obj.pkg_name)
                    old_context_obj.version_name = single_context.get('version_name', old_context_obj.version_name)
                    old_context_obj.version_code = single_context.get('version_code', old_context_obj.version_code)
                    old_context_obj.label = single_context.get('label', old_context_obj.label)
                    old_context_obj.signatures = single_context.get('signatures', old_context_obj.signatures)
                    old_context_obj.save()
                    new_context_obj = old_context_obj
                else:
                    new_context_obj = Context.objects.create(app=app_node, **single_context)

                self.update_meta_data(new_context_obj, md_data)

    def update_meta_data(self, context, md_data):
        if not context:
            return

        for single_md in md_data:
            if single_md:
                expected_md_id = single_md.get('id')
                if expected_md_id:
                    old_md_obj = MetaData.objects.get(id=expected_md_id, context=context)
                    old_md_obj.name = single_md.get('name', old_md_obj.name)
                    old_md_obj.value = single_md.get('value', old_md_obj.value)
                    old_md_obj.save()
                else:
                    MetaData.objects.create(context=context, **single_md)
