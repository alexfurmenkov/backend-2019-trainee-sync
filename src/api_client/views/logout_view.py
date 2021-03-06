from rest_framework.authentication import get_authorization_header

from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.models import Token


class Logout(APIView):
    @classmethod
    def post(cls, request) -> Response:
        """
        JWT logout
        :return: Response dict
        """
        TokenAuthentication.get(request)
        auth_token = get_authorization_header(request).split()

        access_token = Token.objects.get(access_token=auth_token[0])
        access_token.delete()

        return Response('You are logged out.', status=200)
