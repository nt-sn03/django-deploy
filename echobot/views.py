from django.http import HttpRequest, HttpResponse
import json
from pprint import pprint
from .bot import handle_udpate


def webhook(request: HttpRequest) -> HttpResponse:
    data = json.loads((request.body.decode()))

    handle_udpate(data)

    return HttpResponse("Bot is runnning....")
