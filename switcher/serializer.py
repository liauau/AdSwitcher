from rest_framework import serializers
from .models import AppNode, Context, Mix, PlacementMappings


class PlacementMappingsSerializer(serializers.ModelSerializer):
    # mix = serializers.ReadOnlyField(source='mix.id')

    class Meta:
        model = PlacementMappings
        fields = ('id', 'platform', 'placement')
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class MixSerializer(serializers.ModelSerializer):
    placement_mappings = PlacementMappingsSerializer(many=True)

    class Meta:
        model = Mix
        fields = ('default_platform', 'placement_mappings')


class ContextSerializer(serializers.ModelSerializer):
    # app = serializers.ReadOnlyField(source='app.pkg_name')

    class Meta:
        model = Context
        fields = ('id', 'platform', 'pkg_name', 'version_name', 'version_code',
                  'label', 'signatures')
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class AppNodeSerializer(serializers.ModelSerializer):
    pkg_name = serializers.CharField(max_length=255)
    owner = serializers.ReadOnlyField(source='owner.username')
    context = ContextSerializer(many=True)
    mix = MixSerializer()

    class Meta:
        model = AppNode
        fields = ('pkg_name', 'owner', 'mix', 'context')

    def create(self, validated_data):
        mix_data = validated_data.pop('mix')
        placement_mappings_data = mix_data.pop('placement_mappings')
        context_data = validated_data.pop('context')

        app_node = AppNode.objects.create(**validated_data)

        mix = Mix.objects.create(app=app_node, **mix_data)

        for contextItem in context_data:
            Context.objects.create(app=app_node, **contextItem)

        for placement_mappings in placement_mappings_data:
            PlacementMappings.objects.create(mix=mix, **placement_mappings)
        return app_node

    def update(self, instance, validated_data):
        mix_data = validated_data.pop('mix')
        placement_mappings_data = mix_data.pop('placement_mappings')
        context_data = validated_data.pop('context')
        mix = instance.mix

        self.update_appnode(instance, validated_data)
        self.update_mix(mix, mix_data)
        self.update_pm(mix, placement_mappings_data)
        self.update_context(instance, context_data)
        return instance

    @staticmethod
    def update_appnode(app_node, appnode_data):
        app_node.pkg_name = appnode_data.get('pkg_name', app_node.pkg_name)
        app_node.save()

    @staticmethod
    def update_mix(mix, mix_data):
        mix.default_platform = mix_data.get('default_platform', mix.default_platform)
        mix.save()

    @staticmethod
    def update_pm(mix, placement_mappings_data):
        for single_pm in placement_mappings_data:
            if single_pm:
                expected_pm_id = single_pm.get('id', None)
                if expected_pm_id:
                    old_pm_obj = PlacementMappings.objects.get(id=expected_pm_id, mix=mix)
                    old_pm_obj.platform = single_pm.get('platform', old_pm_obj.platform)
                    old_pm_obj.placement = single_pm.get('placement', old_pm_obj.placement)
                    old_pm_obj.save()
                else:
                    PlacementMappings.objects.create(mix=mix, **single_pm)

    @staticmethod
    def update_context(app_node, context_data):
        for single_context in context_data:
            if single_context:
                expected_context_id = single_context.get('id')
                if expected_context_id:
                    old_context_obj = Context.objects.get(id=expected_context_id, app=app_node)
                    old_context_obj.platform = single_context.get('platform', old_context_obj.platform)
                    old_context_obj.pkg_name = single_context.get('pkg_name', old_context_obj.pkg_name)
                    old_context_obj.version_name = single_context.get('version_name', old_context_obj.version_name)
                    old_context_obj.version_code = single_context.get('version_code', old_context_obj.version_code)
                    old_context_obj.label = single_context.get('label', old_context_obj.label)
                    old_context_obj.signatures = single_context.get('signatures', old_context_obj.signatures)
                    old_context_obj.save()
                else:
                    Context.objects.create(app=app_node, **context_data)
