import hashlib

import django
from rest_framework.views import APIView

from rest_framework.response import Response
from pitter.decorators import request_post_serializer
from api_client.validation_serializers.user_serializers import ReistrationPostRequest, DeletePostRequest
from pitter.models import User


class Registration(APIView):
    @classmethod
    @request_post_serializer(ReistrationPostRequest)
    def post(cls, request) -> Response:
        try:
            user_query = request.data
            login = user_query['login']
            password = hashlib.sha256(user_query['password'].encode('utf-8')).hexdigest()
            profile_name = user_query['profile_name']
            email_address = user_query['email_address']
            email_notifications_mode = user_query['email_notifications_mode']
            User.create_user(login, password, profile_name, email_address, email_notifications_mode)
            returned_data = dict(
                login=login,
                profile_name=profile_name,
                email_address=email_address,
            )
            return Response(returned_data, status=200)
        except django.db.utils.IntegrityError:
            return Response('User already exists.')

    @classmethod
    @request_post_serializer(DeletePostRequest)
    def delete(cls, request) -> Response:
        user_query = request.data
        id = user_query['id']

        try:
            user_do_delete = User.objects.get(id=id)
            user_do_delete.delete()
            returned_data = dict(
                login=user_do_delete.login,
                profile_name=user_do_delete.profile_name,
                email_address=user_do_delete.email_address,
            )
            return Response(returned_data, status=200)
        except User.DoesNotExist:
            return Response('User is not found.')



