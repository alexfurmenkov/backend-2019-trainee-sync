from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.decorators import request_post_serializer
from pitter.models import Pitt
from api_client.validation_serializers.pitt_serializers import SavePittRequest


class SavePitt(APIView):
    @classmethod
    @request_post_serializer(SavePittRequest)
    def post(cls, request) -> Response:
        """
        Saves a Pitt to the DB
        :param request:
        :return: Response dict
        """
        data = request.data
        user_id = data['user_id']
        audio_path = data['audio_path']
        audio_decoded = data['audio_decoded']
        Pitt.create_pitt(user_id, audio_path, audio_decoded)
        return Response(data)
