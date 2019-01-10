from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from eventbrite import Eventbrite
import json
from django.core.serializers.json import DjangoJSONEncoder

@require_POST
@csrf_exempt
def eventbrite(request):
    # json_string = request
    data = json.loads(request.body)
    # data = json.dumps(json_string)
    # print(data)

    print(data)
    return HttpResponse('success')



    # api_url = data["api_url"]
    #
    # print(api_url)



# def eventbrite(request):
#     return JsonResponse (request.body,safe=False)
#     data = json.loads(request)
#     api_url = data.get('api_url', None)
#
#     event = Event(api_url)
#     event.save()
#     return HttpResponse("webhook received by ISA")



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
