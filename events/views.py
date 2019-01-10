from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from eventbrite import Eventbrite

@csrf_exempt
def eventbrite(request):
    # return HttpResponse (request.body)
    data = json.loads(request.body)
    api_url = data.get('api_url', None)

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
