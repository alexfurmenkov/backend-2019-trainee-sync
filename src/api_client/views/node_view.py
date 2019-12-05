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
        subscription_flag = params['subscription_flag']
        token = params['token'][2:-1]

        data = {'login': user_login, 'subscription_flag': subscription_flag}
        url = 'http://localhost:8000/follow/'
        headers = {'Authorization': token}
        requests.post(url=url, headers=headers, data=data)

        returned_data = dict(
            text='you are subscribed',
            login=user_login,
        )
        return Response(returned_data, status=200)
