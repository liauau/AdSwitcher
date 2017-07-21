from rest_framework import serializers

from switcher.models.constant import PKG_NAME, PROBABILITY, CONTEXT, \
    VERSION_NAME, VERSION_CODE, LABEL, SIGNATURES, META_DATA, NAME, VALUE
from switcher.models.jh_crack import JhNode, JhContext, JhMetaData


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JhMetaData
        fields = ('id', NAME, VALUE)
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class JhContextSerializer(serializers.ModelSerializer):
    md = MetaDataSerializer(many=True)

    class Meta:
        model = JhContext
        fields = (PKG_NAME, VERSION_NAME, VERSION_CODE, LABEL, SIGNATURES, META_DATA)


class JhNodeSerializer(serializers.ModelSerializer):
    c = JhContextSerializer()

    class Meta:
        model = JhNode
        fields = (PKG_NAME, PROBABILITY, CONTEXT)

    def create(self, validated_data):
        context_data = validated_data.pop(CONTEXT)
        meta_data = context_data.pop(META_DATA)

        # create node
        jh_node = JhNode.objects.create(**validated_data)

        # create context
        jh_context = JhContext.objects.create(jh_node=jh_node, **context_data)

        # create meta_data
        for meta in meta_data:
            JhMetaData.objects.create(c=jh_context, **meta)

        return jh_node

    def update(self, instance, validated_data):
        context_data = validated_data.pop(CONTEXT)
        self.update_node(instance, validated_data)
        self.update_context(instance, context_data)
        return instance

    def update_node(self, instance, validated_data):
        instance.pro = validated_data.get(PROBABILITY, instance.pro)
        instance.save()

    def update_context(self, jh_node, context_data):
        meta_data = context_data.pop(META_DATA)
        context_obj = JhContext.objects.get(jh_node=jh_node)
        context_obj.p = context_data.get(PKG_NAME, context_obj.p)
        context_obj.vn = context_data.get(VERSION_NAME, context_obj.vn)
        context_obj.vc = context_data.get(VERSION_CODE, context_obj.vc)
        context_obj.l = context_data.get(LABEL, context_obj.l)
        context_obj.sg = context_data.get(SIGNATURES, context_obj.sg)
        context_obj.save()
        self.update_meta_data(context_obj, meta_data)

    def update_meta_data(self, context, meta_data):
        for meta in meta_data:
            if meta:
                expected_meta_id = meta.get('id', None)
                if expected_meta_id:
                    old_meta_obj = JhMetaData.objects.get(id=expected_meta_id, c=context)
                    old_meta_obj.nm = meta.get(NAME, old_meta_obj.nm)
                    old_meta_obj.vl = meta.get(VALUE, old_meta_obj.vl)
                    old_meta_obj.save()
                else:
                    JhMetaData.objects.create(c=context, **meta)
