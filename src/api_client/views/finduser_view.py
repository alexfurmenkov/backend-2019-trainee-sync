from rest_framework.authentication import get_authorization_header
from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.acc_actions.auth import TokenAuthentication
from pitter.models import Pitt, Follower
from pitter.models.user_model import User
from pitter.decorators import request_query_serializer

from api_client.validation_serializers.user_serializers import FindRequest


class FindUser(APIView):
    @classmethod
    @request_query_serializer(FindRequest)
    def get(cls, request) -> Response:
        """
        Finds user in the DB with the login from the query
        :param request:
        :return: Response dict with the user data
        """
        access = TokenAuthentication.get(request)
        auth_token = get_authorization_header(request).decode('utf-8')

        data = request.query_params
        login = data['login']
        feed_pitts = []
        follow_link = f'http://localhost:8000/follownode/?login={login}&token={auth_token}'
        unfollow_link = f'http://localhost:8000/follownode/?login={login}&unfollow=True&token={auth_token}'

        try:
            user = User.objects.get(login=login)
            follower = User.objects.get(email_address=access['email'])

        except User.DoesNotExist:
            return Response('User is not found.', status=200)
        except KeyError:
            return Response('Yiu are logged out.', status=200)

        for pitt in Pitt.objects.all():
            if pitt.user_id == user.id:
                pitt_info = (pitt.audio_decoded, pitt.created_at)
                feed_pitts.append(pitt_info)

        returned_data = dict(
            id=user.id,
            login=user.login,
            email=user.email_address,
            pitts=feed_pitts,
        )

        try:
            follower_exists = Follower.objects.get(user_id=user.id, follower_id=follower.id)
            if follower_exists:
                returned_data['unfollow_link'] = unfollow_link
            return Response(returned_data, status=200)

        except Follower.DoesNotExist:
            returned_data['follow_link'] = follow_link
            return Response(returned_data, status=200)
