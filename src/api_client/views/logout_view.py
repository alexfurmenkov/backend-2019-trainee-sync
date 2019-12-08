import jwt

from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.acc_actions.keys import private_k


class Logout(APIView):
    @classmethod
    def post(cls, request) -> Response:
        """
        JWT logout
        :param request:
        :return: Response dict
        """
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        email = access['email']
        name = access['name']
        token_lifetime = 0

        payload = {
            'email': email,
            'name': name,
            'exp': token_lifetime,
        }
        token = jwt.encode(payload, private_k, algorithm='RS256')
        data = dict(
            token=token,
        )
        return Response(data, status=200)
