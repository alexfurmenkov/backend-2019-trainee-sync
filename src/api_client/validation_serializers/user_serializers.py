from rest_framework import serializers


class ReistrationPostRequest(serializers.Serializer):
    """
    Reistration serializer
    """
    login = serializers.CharField(required=True, label='login', max_length=256)
    password = serializers.CharField(required=True, label='password', max_length=256)
    profile_name = serializers.CharField(required=True, label='profile_name', max_length=256)
    email_address = serializers.CharField(required=True, label='email_address', max_length=256)
    email_notifications_mode = serializers.BooleanField(required=True, label='email_notifications_mode')


class DeleteAccountRequest(serializers.Serializer):
    """
    Delete account serializer
    """
    id = serializers.CharField(required=True, label='id', max_length=256)


class UserPostRequest(serializers.Serializer):
    """
    Login serializer
    """
    login = serializers.CharField(required=True, label='Login', max_length=256)
    password = serializers.CharField(required=True, label='Password', max_length=256)


class FollowPostRequest(serializers.Serializer):
    """
    Folllow serializer
    """
    login = serializers.CharField(required=True, label='login', max_length=256)


class DeleteRequest(serializers.Serializer):
    """
    Unfolllow serializer
    """
    login = serializers.CharField(required=True, label='login', max_length=256)


class FindRequest(serializers.Serializer):
    """
    Find user serializer
    """
    login = serializers.CharField(required=True, label='login', max_length=256)


class FeedRequest(serializers.Serializer):
    """
    Feed serializer
    """
    time = serializers.IntegerField(required=False, label='time')


class NodeRequest(serializers.Serializer):
    """
    Follow node serializer
    """
    login = serializers.CharField(required=True, label='login', max_length=256)
    subscription_flag = serializers.BooleanField(required=True, label='subscription_flag')


class DeleteNodeRequest(serializers.Serializer):
    """
    Delete account node serializer
    """
    id = serializers.CharField(required=True, label='login', max_length=256)
