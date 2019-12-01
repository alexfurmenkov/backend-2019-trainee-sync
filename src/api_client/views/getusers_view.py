from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.models.user_model import User
from pitter.decorators import request_post_serializer

from api_client.validation_serializers.user_serializers import GetUsersRequest


class GetUsers(APIView):
    @classmethod
    @request_post_serializer(GetUsersRequest)
    def post(cls, request) -> Response:
        """
        Used to diaplay all users
        :param request:
        :return: Response dict
        """
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        all_users = User.objects.all()
        users_list = [x.login for x in all_users]
        returned_data = dict(
            users_list=users_list,
        )
        return Response(returned_data, status=200)
