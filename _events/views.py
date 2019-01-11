from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from eventbrite import Eventbrite
import json
from django.core.serializers.json import DjangoJSONEncoder
from events.models import Event

@csrf_exempt
def eventbrite(request):
    # return HttpResponse (request.body)
    #thing = request.body.read.decode("utf-8")
    #data = json.loads(thing)

    #data = json.loads(request.body)
    data = request.body.decode('utf-8')
    data  = json.loads(data)
    # print (data)
    # api_url = data.get('api_url', None)
    #
    api_url = data['api_url']
    print (type(api_url))
    print (api_url)
    # #
    event = Event(api_url=api_url)
    event.save()

    return HttpResponse("webhook received by ISA")



# def webhook():
#
#
#     # Use the API client to convert from a webhook to an API object
#     api_object = eventbrite.webhook_to_object(request)
#
#     # Process the API object
#     if api_object.type == 'User':
#         do_user_process(api_object)
#
#     if api_object.type == 'Event':
#         do_event_process(api_object)
#
#         print(api_object)
#
#     return ""
