from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header

import jwt

from pitter.models import Token
from .keys import public_k


class TokenAuthentication(APIView):
    auth_token = ''

    @staticmethod
    def get(request):
        auth_token = get_authorization_header(request).split()
        if not auth_token:
            raise exceptions.AuthenticationFailed('Token is not set.')

        else:
            try:
                token_valid = Token.objects.get(access_token=auth_token[0])

            except Token.DoesNotExist:
                return dict(
                    message='Token has expired.'
                )

            if token_valid:
                payload = jwt.decode(auth_token[0], public_k, algorithm='RS256')

                email = payload['email']
                name = payload['name']
                exp = payload['exp']
                return dict(
                    email=email,
                    name=name,
                    exp=exp,
                )
            else:
                raise exceptions.AuthenticationFailed('You are logged out.')