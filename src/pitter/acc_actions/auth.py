from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
import jwt
from .keys import public_k


class TokenAuthentication(APIView):
    auth_token = ''

    def get(self, request):
        auth_token = get_authorization_header(request).split()
        if not auth_token:
            raise exceptions.AuthenticationFailed('Token is not set')

        else:
            payload = jwt.decode(auth_token[0], public_k, algorithm='RS256')
            email = payload['email']
            name = payload['name']
            return dict(
                email=email,
                name=name,
            )