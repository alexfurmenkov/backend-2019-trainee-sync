import requests
from rest_framework.views import APIView

from pitter.acc_actions.auth import TokenAuthentication
from pitter.models import Follower
from pitter.models.user_model import User
from rest_framework.response import Response
from pitter.decorators import request_post_serializer
from api_client.validation_serializers.user_serializers import FollowPostRequest


class Follow(APIView):
    @classmethod
    @request_post_serializer(FollowPostRequest)
    def post(cls, request) -> Response:
        user_auth = TokenAuthentication()
        access = user_auth.get(request)

        data = request.data
        subscription_flag = data['subscription_flag']
        subscriber_email = access['email']
        user_login = data['login']

        try:
            find_follower = User.objects.get(email_address=subscriber_email)
            follower_id = find_follower.id
            find_user = User.objects.get(login=user_login)
            user_id = find_user.id

            user_email = find_user.email_address
            follower_login = find_follower.login

            r = requests.post(
                url="https://api.mailgun.net/v3/sandboxb3f7b13f20844cedaf8e5a0e05cdb824.mailgun.org/messages",
                auth=("api", "3adac155c921fea3423695a3acee1e58-e470a504-39684050"),
                data={"from": "mailgun@sandboxb3f7b13f20844cedaf8e5a0e05cdb824.mailgun.org",
                      "to": user_email,
                      "subject": "New follower",
                      "text": f'You have one new follower. His login: {follower_login}'}
            )
            Follower.create_follower(user_id, follower_id, subscription_flag)
            returned_data = dict(
                user_id=user_id,
                follower_id=follower_id,
                subscription_flag=subscription_flag,
            )
            return Response(returned_data, status=200)
        except User.DoesNotExist:
            return Response('User is not found.')

    @classmethod
    @request_post_serializer(FollowPostRequest)
    def delete(cls, request) -> Response:
        login = request.data['login']
        user = User.objects.get(login=login)
        user_id = user.id
        user_do_delete = Follower.objects.get(user_id=user_id)
        user_do_delete.delete()
        return Response(login)
