from rest_framework import serializers


class PittRequest(serializers.Serializer):
    """
    Making Pitt serializer
    """
    audio_path = serializers.CharField(required=True, label='audio_path', max_length=256)


class SavePittRequest(serializers.Serializer):
    """
    Saving Pitt to DB serializer
    """
    user_id = serializers.CharField(required=True, label='audio_path', max_length=256)
    audio_path = serializers.CharField(required=True, label='audio_path', max_length=256)
    audio_decoded = serializers.CharField(required=True, label='audio_decoded', max_length=256)


class DeletePittRequest(serializers.Serializer):
    """
    Deleting Pitt serializer
    """
    id = serializers.CharField(required=True, label='id', max_length=256)
