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
        user_auth = TokenAuthentication()
        access = user_auth.get(request)
        params = request.query_params
        feed_pitts = []
        users = []

        follower_email = access['email']
        follower = User.objects.get(email_address=follower_email)
        follower_id = follower.id
        follower_login = follower.login

        all_followers = Follower.objects.all()
        all_pitts = Pitt.objects.all()

        for foll in all_followers:
            if foll.follower_id == follower_id:
                users.append(foll.user_id)

        for pitt in all_pitts:
            for user_id in users:
                if pitt.user_id == user_id:
                    user = User.objects.get(id=user_id)
                    user_login = user.login
                    user_profile = f'http://localhost:8000/finduser/?login={user_login}'
                    pitt_info = [user_login, user_profile, pitt.audio_decoded, pitt.created_at, pitt.id]
                    feed_pitts.append(pitt_info)

            if pitt.user_id == follower_id:
                follower_profile = f'http://localhost:8000/finduser/?login={follower_login}'
                pitt_info = [follower_login, follower_profile, pitt.audio_decoded, pitt.created_at, pitt.id]
                feed_pitts.append(pitt_info)

        feed_pitts.reverse()
        feed = Paginator(feed_pitts, 2)

        if 'page' in params:
            query_page = params['page']
            page_number = query_page
        else:
            page_number = 1

        try:
            page = feed.page(page_number)
            return Response(page.object_list, status=200)

        except django.core.paginator.EmptyPage:
            return Response('This page is not existing', status=200)
