import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.decorators import request_query_serializer

from api_client.validation_serializers.user_serializers import NodeRequest


class Node(APIView):
    @classmethod
    @request_query_serializer(NodeRequest)
    def get(cls, request) -> Response:
        """
        Follow node
        :return: Response with the result of subscription
        """
        params = request.query_params
        user_login = params['login']
        token = params['token'][2:-1]

        url = 'http://localhost:8000/follow/'
        headers = {'Authorization': token}

        if 'unfollow' in params:
            data = {'login': user_login}
            requests.delete(url=url, headers=headers, data=data)
            returned_data = dict(
                text='you are unsubscribed',
                login=user_login,
            )
        else:
            data = {'login': user_login, 'subscription_flag': params['subscription_flag']}
            requests.post(url=url, headers=headers, data=data)
            returned_data = dict(
                text='you are subscribed',
                login=user_login,
            )
        return Response(returned_data, status=200)
