from rest_framework.views import APIView

from pitter.acc_actions.auth import TokenAuthentication
from pitter.models.user_model import User
from rest_framework.response import Response
from pitter.decorators import request_post_serializer
from api_client.validation_serializers.user_serializers import FindPostRequest


class FindUser(APIView):
    @classmethod
    @request_post_serializer(FindPostRequest)
    def post(cls, request) -> Response:
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        data = request.data
        login = data['login']
        try:
            user = User.objects.get(login=login)
            returned_data = dict(
                login=user.login,
                email=user.email_address,
            )
            return Response(returned_data)
        except User.DoesNotExist:
            return Response('User is not found.')
