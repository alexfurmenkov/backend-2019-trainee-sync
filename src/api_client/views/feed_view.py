import django
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.paginator import Paginator

from pitter.decorators import request_query_serializer
from pitter.acc_actions.auth import TokenAuthentication
from pitter.models.user_model import User
from pitter.models.follower_model import Follower
from pitter.models.pitt_model import Pitt

from api_client.validation_serializers.user_serializers import FeedRequest


class Feed(APIView):
    @classmethod
    @request_query_serializer(FeedRequest)
    def get(cls, request) -> Response:
        """
        Displays the feed
        :return: Response with the list of the pitts
        """
        access = TokenAuthentication.get(request)
        feed_pitts = []
        users = []

        try:
            follower_email = access['email']
        except KeyError:
            return Response('You are logged out.', status=200)

        follower = User.objects.get(email_address=follower_email)

        for foll in Follower.objects.all():
            if foll.follower_id == follower.id:
                users.append(foll.user_id)

        for pitt in Pitt.objects.all():
            for user_id in users:
                if pitt.user_id == user_id:
                    user = User.objects.get(id=user_id)
                    pitt_info = [user.login, f'http://localhost:8000/finduser/?login={user.login}',
                                 pitt.audio_decoded, pitt.created_at, pitt.id]
                    feed_pitts.append(pitt_info)

            if pitt.user_id == follower.id:
                pitt_info = [follower.login, f'http://localhost:8000/finduser/?login={follower.login}',
                             pitt.audio_decoded, pitt.created_at, pitt.id]
                feed_pitts.append(pitt_info)

        feed_pitts.reverse()
        feed = Paginator(feed_pitts, 2)

        if 'page' in request.query_params:
            page_number = request.query_params['page']
        else:
            page_number = 1

        try:
            page = feed.page(page_number)
            return Response(page.object_list, status=200)

        except django.core.paginator.EmptyPage:
            return Response('This page does not exist', status=200)
