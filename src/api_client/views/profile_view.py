from rest_framework.authentication import get_authorization_header
from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.models.user_model import User


class Profile(APIView):
    @classmethod
    def get(cls, request) -> Response:
        """
        User profile
        :return: Response dict with the user's data
        """
        access = TokenAuthentication.get(request)
        auth_token = get_authorization_header(request)

        user_email = access['email']
        user_profile_name = access['name']
        user = User.objects.get(email_address=user_email, profile_name=user_profile_name)

        feed_link = 'http://localhost:8000/feed/'
        makepitt_link = 'http://localhost:8000/makepitt/'
        finduser_link = 'http://localhost:8000/finduser/'
        all_users_link = 'http://localhost:8000/users/'
        logout_link = 'http://localhost:8000/logout/'
        delete_link = f'http://localhost:8000/deletenode/?id={user.id}&token={auth_token}'

        returned_data = dict(
            user_data=dict(
                id=user.id,
                login=user.login,
                profile_name=user_profile_name,
                email_address=user_email,
            ),
            functions=dict(
                feed=feed_link,
                pitt=makepitt_link,
                find_user=finduser_link,
                all_users=all_users_link,
                logout=logout_link,
                delete_account=delete_link,
            ),
        )

        return Response(returned_data, status=200)
