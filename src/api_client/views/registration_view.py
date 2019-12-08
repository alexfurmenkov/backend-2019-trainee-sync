import hashlib

from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.decorators import request_post_serializer
from pitter.models import User
from api_client.validation_serializers.user_serializers import ReistrationPostRequest, DeleteAccountRequest


class Registration(APIView):
    @classmethod
    @request_post_serializer(ReistrationPostRequest)
    def post(cls, request) -> Response:
        """
        Registers a new user
        :return: Response dict with the new user's data
        """
        data = request.data
        login = data['login']
        password = hashlib.sha256(data['password'].encode('utf-8')).hexdigest()
        profile_name = data['profile_name']
        email_address = data['email_address']
        email_notifications_mode = data['email_notifications_mode']

        try:
            existing_user = User.objects.get(login=login)
            if existing_user:
                return Response('User with this login already exists.', status=200)
        except User.DoesNotExist:
            User.create_user(login, password, profile_name, email_address, email_notifications_mode)

        returned_data = dict(
            message='You are registered!',
            login=login,
            profile_name=profile_name,
            email_address=email_address,
        )
        return Response(returned_data, status=200)

    @classmethod
    @request_post_serializer(DeleteAccountRequest)
    def delete(cls, request) -> Response:
        """
        Deletes existing user
        :return: Response dict
        """
        user_query = request.data
        user_id = user_query['id']

        try:
            user_do_delete = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response('User is not found.')

        user_do_delete.delete()
        returned_data = dict(
            login=user_do_delete.login,
            profile_name=user_do_delete.profile_name,
            email_address=user_do_delete.email_address,
        )
        return Response(returned_data, status=200)

