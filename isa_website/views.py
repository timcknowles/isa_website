import datetime
import os
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from eventbrite import Eventbrite

from home.models import Event

#set the token
eventtoken = os.environ.get('EVENTBRITE_TOKEN')
eventbrite = Eventbrite(eventtoken)


@csrf_exempt
def eventbrite(request):
    # return HttpResponse (request.body)
    print (request.body)
    #data = json.loads(request.body)
    data = request.body
    api_url = data.get('api_url', None)

    print (api_url)

    event = Event(api_url)
    event.save()
    return HttpResponse("webhook received by ISA")



# @app.route('/eventbrite', methods=['POST'])
def webhook():

    # Use the API client to convert from a webhook to an API object
    api_object = eventbrite.webhook_to_object(request)

    # Process the API object
    if api_object.type == 'User':
        do_user_process(api_object)

    if api_object.type == 'Event':
        do_event_process(api_object)

    return ""


def event_view(request):

    # #isa_events = eventbrite.get_organizers_events(12665608962)
    # isa_events = eventbrite.event_search(**{'organizer.id':12665608962})
    # # print (isa_events['events'])
    # for i in isa_events['events']:
    #     print (i['name']['text'])
    #     html += "<br> %s" % i['name']['text']
    events = Event.object.all()

    return HttpResponse(html)
