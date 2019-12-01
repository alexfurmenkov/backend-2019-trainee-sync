import hashlib
import jwt

from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.models.user_model import User
from pitter.acc_actions.keys import private_k
from pitter.decorators import request_post_serializer

from api_client.validation_serializers.user_serializers import UserPostRequest


class Login(APIView):
    @classmethod
    @request_post_serializer(UserPostRequest)
    def post(cls, request) -> Response:
        """
        JWT authentification
        :param request:
        :return: Response dict
        """
        login = request.data['login']
        password = hashlib.sha256(request.data['password'].encode('utf-8')).hexdigest()

        try:
            user = User.objects.get(login=login, password=password)

            if user:
                payload = {
                    'email': user.email_address,
                    'name': user.profile_name,
                }
                token = jwt.encode(payload, private_k, algorithm='RS256')
                returned_data = dict(
                    token=token,
                    email=payload['email'],
                    name=payload['name'],
                )
                response = Response(returned_data, status=200)
                return response
        except User.DoesNotExist:
            return Response('User is not found.')
