from rest_framework import serializers
from .models import Stat, Event


class EventSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    log_time = serializers.IntegerField()
    params = serializers.JSONField()

    class Meta:
        model = Event
        fields = ('id', 'name', 'log_time', 'params')
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class StatSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(max_length=255)
    android_id = serializers.CharField(max_length=255)
    google_ad_id = serializers.CharField(max_length=255)
    referer = serializers.CharField(max_length=255)
    time_offset = serializers.IntegerField(default=0)
    locale = serializers.CharField(max_length=255)
    events = EventSerializer(many=True)

    class Meta:
        model = Stat
        fields = ('user_id', 'android_id', 'google_ad_id', 'referer', 'time_offset', 'locale', 'events')

    def create(self, validated_data):
        events_data = validated_data.pop('events')
        stat = Stat.objects.create(**validated_data)

        for event in events_data:
            Event.objects.create(stat=stat, **event)

        return stat

    def update(self, instance, validated_data):
        events_data = validated_data.pop('events')

        self.updateStat(instance, **validated_data)
        self.updateEvents(instance, **events_data)

    def update_stat(self, stat, stat_data):
        stat.user_id = stat_data.get('user_id', stat.user_id)
        stat.android_id = stat_data.get('android_id', stat.android_id)
        stat.google_ad_id = stat_data.get('google_ad_id', stat.google_ad_id)
        stat.referer = stat_data.get('referer', stat.referer)
        stat.time_offset = stat_data.get('time_offset', stat.time_offset)
        stat.locale = stat_data.get('locale', stat.locale)
        stat.save()

    def update_events(self, stat, events_data):
        for event in events_data:
            if event:
                expected_event_id = event.get('id', None)
                if expected_event_id:
                    old_event_obj = Event.objects.get(id=expected_event_id, stat=stat)
                    old_event_obj.name = event.get('name', old_event_obj.name)
                    old_event_obj.log_time = event.get('log_time', old_event_obj.log_time)
                    old_event_obj.params = event.get('params', old_event_obj.params)
                    old_event_obj.save()
                else:
                    Event.objects.create(stat=stat, **event)
