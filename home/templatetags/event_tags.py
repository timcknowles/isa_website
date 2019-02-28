from django import template
from home.models import Event

register = template.Library()

...

# Advert snippets
@register.inclusion_tag('home/tags/events.html', takes_context=True)
def event(context):
    return {
        'event': Event.objects.all(),
        'request': context['request'],
    }
