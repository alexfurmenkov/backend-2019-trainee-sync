from rest_framework.views import APIView
from pitter.acc_actions.auth import TokenAuthentication
from pitter.models.user_model import User
from pitter.models.follower_model import Follower
from pitter.models.pitt_model import Pitt
from rest_framework.response import Response
from pitter.decorators import request_post_serializer
from api_client.validation_serializers.user_serializers import FeedRequest
import datetime


class Feed(APIView):
    @classmethod
    @request_post_serializer(FeedRequest)
    def post(cls, request) -> Response:
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        profile_name = access['name']
        follower = User.objects.get(profile_name=profile_name)
        follower_id = follower.id
        follower_object = Follower.objects.get(follower_id=follower_id)
        user_id = follower_object.user_id
        all_pitts = Pitt.objects.all()
        feed_pitts = []
        paginated_pitts = []

        for pitt in all_pitts:
            if pitt.user_id == user_id:
                pitt_info = (pitt.audio_decoded, pitt.created_at)
                feed_pitts.append(pitt_info)
            else:
                continue

        if request.data['time']:
            current_time = datetime.datetime.now()
            for pitt in feed_pitts:
                if (current_time.hour - pitt[1].hour) < request.data['time']:
                    paginated_pitts.append(pitt[0])
            return Response(paginated_pitts, status=200)

        elif not request.data['time']:
            return Response(feed_pitts, status=200)


