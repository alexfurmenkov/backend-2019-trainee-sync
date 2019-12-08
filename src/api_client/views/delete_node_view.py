import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from pitter.decorators import request_query_serializer

from api_client.validation_serializers.user_serializers import DeleteNodeRequest


class DeleteNode(APIView):
    @classmethod
    @request_query_serializer(DeleteNodeRequest)
    def get(cls, request) -> Response:
        """
        Follow node
        :return: Response with the result of deleting
        """
        params = request.query_params
        user_id = params['id']
        token = params['token'][2:-1]

        url = 'http://localhost:8000/registration/'
        headers = {'Authorization': token}
        data = {'id': user_id}
        requests.delete(url=url, headers=headers, data=data)

        returned_data = dict(
            text='account is deleted',
        )
        return Response(returned_data, status=200)
