from rest_framework import serializers


class PittRequest(serializers.Serializer):
    audio_path = serializers.CharField(required=True, label='audio_path', max_length=256)


class SavePittRequest(serializers.Serializer):
    user_id = serializers.CharField(required=True, label='audio_path', max_length=256)
    audio_path = serializers.CharField(required=True, label='audio_path', max_length=256)
    audio_decoded = serializers.CharField(required=True, label='audio_decoded', max_length=256)


