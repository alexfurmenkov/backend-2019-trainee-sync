from rest_framework import serializers


class FindPostRequest(serializers.Serializer):
    login = serializers.CharField(required=True, label='login', max_length=256)
