from rest_framework import serializers


class ReistrationPostRequest(serializers.Serializer):
    login = serializers.CharField(required=True, label='login', max_length=256)
    password = serializers.CharField(required=True, label='password', max_length=256)
    profile_name = serializers.CharField(required=True, label='profile_name', max_length=256)
    email_address = serializers.CharField(required=True, label='email_address', max_length=256)
    email_notifications_mode = serializers.BooleanField(required=True, label='email_notifications_mode')


class DeletePostRequest(serializers.Serializer):
    id = serializers.CharField(required=True, label='id', max_length=256)
