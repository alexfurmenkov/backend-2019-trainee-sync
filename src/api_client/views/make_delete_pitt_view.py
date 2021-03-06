import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.decorators import request_post_serializer
from pitter.models import User, Pitt

from api_client.validation_serializers.pitt_serializers import PittRequest, DeletePittRequest


class MakeDeletePitt(APIView):
    @classmethod
    @request_post_serializer(PittRequest)
    def post(cls, request) -> Response:
        """
        Makes a pitt
        :return: Response with audio's name
        """
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        try:
            user_email = access['email']
        except KeyError:
            return Response('You are logged out.', status=200)

        user = User.objects.get(email_address=user_email)
        user_id = user.id
        audio_path = request.data['audio_path']

        data = {'user_id': user_id, 'audio_path': audio_path}
        headers = {"Content-Type": "application/json"}
        url = 'http://localhost:8118/voice/'

        try:
            requests.post(url=url, data=data, headers=headers)
            response = Response(data['audio_path'], status=200)
            return response
        except requests.ConnectionError:
            return Response('Unable to connect to the server.')

    @classmethod
    @request_post_serializer(DeletePittRequest)
    def delete(cls, request) -> Response:
        """
        Deletes a pitt
        :param request:
        :return: Response dict
        """
        access = TokenAuthentication.get(request)

        try:
            access['email']
        except KeyError:
            return Response('You are logged out.', status=200)

        try:
            pitt_id = request.data['id']
            pitt = Pitt.objects.get(id=pitt_id)

        except Pitt.DoesNotExist:
            return Response('Pitt is not found.')

        pitt.delete()
        returned_data = dict(
            id=pitt_id,
        )
        return Response(returned_data, status=200)
