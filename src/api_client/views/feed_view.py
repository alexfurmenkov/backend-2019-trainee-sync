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
        feed_pitts = []
        users = []

        follower_object = Follower.objects.all()
        all_pitts = Pitt.objects.all()
        params = request.query_params

        for foll in follower_object:
            users.append(foll.user_id)

        for pitt in all_pitts:
            for user_id in users:
                if pitt.user_id == user_id:
                    user = User.objects.get(id=user_id)
                    user_login = user.login
                    user_profile = f'http://localhost:8000/finduser/?login={user_login}'
                    pitt_info = [user_login, user_profile, pitt.audio_decoded, pitt.created_at, pitt.id]
                    feed_pitts.append(pitt_info)

        p = Paginator(feed_pitts, 2)

        if 'page' in params:
            query_page = params['page']
            page_number = query_page
        else:
            page_number = 1

        page = p.page(page_number)

        return Response(page.object_list, status=200)
