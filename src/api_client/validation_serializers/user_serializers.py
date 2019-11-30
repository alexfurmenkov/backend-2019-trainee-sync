from rest_framework import serializers


class UserPostRequest(serializers.Serializer):
    login = serializers.CharField(required=True, label='Login', max_length=256)
    password = serializers.CharField(required=True, label='Password', max_length=256)

