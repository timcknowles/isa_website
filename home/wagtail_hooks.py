from django.http import HttpResponse
from wagtail.core import hooks
from .models import EventPage, HomePage
from eventbrite import Eventbrite
import os

#set the token
eventtoken = os.environ.get('EVENTBRITE_TOKEN')
eventbrite = Eventbrite(eventtoken)

@hooks.register('after_create_page')
def do_after_page_create(request, Page):
    if Page.specific_class == EventPage:
        user = eventbrite.get_user()
        events = eventbrite.event_search(**{'user.id': user['id']})
        print (events.pretty)

        return HttpResponse("Congrats on making content!", content_type="text/plain")
