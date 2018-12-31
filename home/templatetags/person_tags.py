from django import template
from home.models import Person

register = template.Library()

...

# Advert snippets
@register.inclusion_tag('home/tags/people.html', takes_context=True)
def people(context):
    return {
        'people': Person.objects.all(),
        'request': context['request'],
    }
