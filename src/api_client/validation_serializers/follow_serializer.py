from rest_framework import serializers


class FollowPostRequest(serializers.Serializer):
    login = serializers.CharField(required=True, label='login', max_length=256)
    subscription_flag = serializers.BooleanField(required=True, label='subscription_flag')
