from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.models.user_model import User


class GetUsers(APIView):
    @classmethod
    def get(cls, request) -> Response:
        """
        Used to diaplay all users
        :return: Response dict
        """
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        all_users = User.objects.all()
        users_list = []

        for user in all_users:
            user_info = {'login': user.login, 'profile': f'http://localhost:8000/finduser/?login={user.login}'}
            users_list.append(user_info)

        returned_data = dict(
            users_list=users_list,
        )
        return Response(returned_data, status=200)
