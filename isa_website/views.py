import datetime
import os
import json
import codecs

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.dateparse import parse_datetime

from eventbrite import Eventbrite

from home.models import Event

#set the token
eventtoken = os.environ.get('EVENTBRITE_TOKEN')

#reader to decode the Http
reader = codecs.getreader("utf-8")

@csrf_exempt
def eventbrite(request):

    data = request.body.decode('utf-8')
    data  = json.loads(data)

    api_url = data['api_url']
    print (api_url)

    event = Event(api_url=api_url)
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
    eventbrite = Eventbrite(eventtoken)
    events = Event.objects.all()

    live_events = [[],[],[],[],[]]

    for i in events:
        try:
            api_object = eventbrite.get(i.api_url)
            print(api_object.pretty)
            try:
                #print (datetime.datetime.strptime(api_object['start']['local']), "%c")
                print(parse_datetime(api_object['start']['local']))
            except:
                print("couldnt do time thing")
            #create dictionary of event
            isa_event = {
                "name": api_object['name']['html'],
                "starttime": parse_datetime(api_object['start']['local']),
                "url": api_object['url'],
            }
            #find which kind of event it is
            #get first 3 characters of event name
            name_code = api_object['name']['html'][0:3]
            name_code = name_code.lower()
            print(name_code)

            #now loop to put event in correct category
            if name_code == "cor":
                live_events[0].append(isa_event)
            elif name_code == "int":
                live_events[1].append(isa_event)
            elif name_code =="hig":
                live_events[2].append(isa_event)
            elif name_code == "fd ":
                #skip faculty development events
                # live_events[3].append(isa_event)
                # print("append")
                pass
            else:
                live_events[3].append(isa_event)

            print (name_code)
            live_events.append(isa_event)
        except:
            print ("bad api url")

    context= {"events": live_events}
    return render(request,'events.html', context)
