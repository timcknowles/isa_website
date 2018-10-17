from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock



class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class EventPage(Page):
    eventname = models.CharField(max_length=255)
    date = models.DateField("event date")
    body = StreamField([
        ('event', blocks.CharBlock(classname="event name")),
        ('description', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('eventname'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]

class EventbritePage(Page):
    event_description = RichTextField(blank=True)
    event_start = models.DateTimeField("event start")
    event_end = models.DateTimeField("event end")


    content_panels = Page.content_panels + [

        FieldPanel('event_start'),
        FieldPanel('event_end'),
        FieldPanel('event_description'),
    ]
