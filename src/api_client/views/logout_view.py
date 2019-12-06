from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.decorators import request_post_serializer

from api_client.validation_serializers.user_serializers import LogoutRequest


class Logout(APIView):
    @classmethod
    @request_post_serializer(LogoutRequest)
    def post(cls, request) -> Response:
        """
        JWT logout
        :param request:
        :return: Response dict
        """
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        data = dict(
            token='',
        )
        return Response(data, status=200)
