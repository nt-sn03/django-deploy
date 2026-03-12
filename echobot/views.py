from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .bot import handle_udpate


class WebHookView(APIView):

    def get(self, request: Request) -> Response:
        return Response(data={'status': 'bot is running...'})

    def post(self, request: Request) -> Response:
        handle_udpate(request.data)

        return Response()
