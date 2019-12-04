from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.models import Pitt
from pitter.models.user_model import User
from pitter.decorators import request_post_serializer

from api_client.validation_serializers.user_serializers import FindPostRequest


class FindUser(APIView):
    @classmethod
    @request_post_serializer(FindPostRequest)
    def get(cls, request) -> Response:
        """
        Finds user in the DB with the login from the query
        :param request:
        :return: Response dict with the user data
        """
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        data = request.data
        login = data['login']
        all_pitts = Pitt.objects.all()
        feed_pitts = []
        follow_link = f'http://localhost:8000/follow/?login={login}&subscription_flag=True'

        try:
            user = User.objects.get(login=login)

        except User.DoesNotExist:
            return Response('User is not found.', status=200)

        for pitt in all_pitts:
            if pitt.user_id == user.id:
                pitt_info = (pitt.audio_decoded, pitt.created_at)
                feed_pitts.append(pitt_info)

        returned_data = dict(
            id=user.id,
            login=user.login,
            email=user.email_address,
            pitts=feed_pitts,
            follow_link=follow_link,
        )
        return Response(returned_data, status=200)

