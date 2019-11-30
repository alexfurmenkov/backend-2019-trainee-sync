import requests

from pitter.acc_actions.auth import TokenAuthentication
from rest_framework.views import APIView

from rest_framework.response import Response
from pitter.decorators import request_post_serializer
from api_client.validation_serializers.pitt_serializer import PittRequest
from pitter.models import User


class MakePitt(APIView):
    @classmethod
    @request_post_serializer(PittRequest)
    def post(cls, request) -> Response:
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        user_email = access['email']
        user = User.objects.get(email_address=user_email)
        user_info = {'user_id': user.id, 'audio_path': 'audio.flac'}
        user_id = user_info['user_id']
        audio_path = request.data['audio_path']
        data = {'user_id': user_id, 'audio_path': audio_path}
        headers = {"Content-Type": "application/json"}
        url = 'http://localhost:8118/voice/'
        try:
            r = requests.post(url=url, data=data, headers=headers)
            response = Response(data['audio_path'], status=200)
            return response
        except requests.RequestException:
            return Response('Unable to connect to the server.')



