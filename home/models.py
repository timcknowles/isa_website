from django.db import models
from django.http import HttpResponse

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core.blocks import (CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,)
from wagtail.admin.forms import WagtailAdminModelForm
from django import forms
from modelcluster.fields import ParentalKey
from wagtail.core.signals import page_published
from news.models import NewsPage


from eventbrite import Eventbrite
import os
import tweepy


#get the tokens

#eventbrite tokens
eventtoken = os.environ.get('EVENTBRITE_TOKEN')
eventbrite = Eventbrite(eventtoken)
#twitter tokens
consumer_token = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')



@register_snippet
class Person(models.Model):
    role = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    person_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        FieldPanel('role'),
        FieldPanel('bio'),
        ImageChooserPanel('person_image')
    ]
    # panels = [
    #     FieldPanel('role'),
    #     FieldPanel('first_name'),
    #     FieldPanel('last_name'),
    #     FieldPanel('bio'),
    #     ImageChooserPanel('person_image'),
    # ]
    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.role)
    # def __str__(self):
    #     return self.role

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class StandardPagePersonPlacement(Orderable, models.Model):
    page = ParentalKey('StandardPage', on_delete=models.CASCADE, related_name='person_placements')
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "person placement"
        verbose_name_plural = "people placement"

    panels = [
        SnippetChooserPanel('person'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.people.text

class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"

class StandardPage(Page):

    section = StreamField([
        ('heading', HeadingBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('embed', EmbedBlock()),
        ('table', TableBlock()),
        ('person', SnippetChooserBlock(Person)),
        ('event', blocks.StaticBlock(admin_text='Latest events: no configuration needed.', template='')),



    ], blank=True)

    person = models.ForeignKey(
        'Person',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    event = models.ForeignKey(
        'Event',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )






    content_panels = Page.content_panels + [
        StreamFieldPanel('section'),
        InlinePanel('person_placements', label="people"),
        # SnippetChooserPanel('event'),



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

#modfy the event snippet to add a custom non model field
class EventForm(WagtailAdminModelForm):
    user_event_id = forms.CharField()

#good place to add validation to check whether event aready exists in DB

#get request on eventbrite api
    def event(self):
        eventbrite = Eventbrite(eventtoken)
        event = eventbrite.get_event('user_event_id')
        print (event.pretty)
        print (event.url)
        print (event.start)

        return event

#autogenrate event model fields from api request




        def save(self, commit=True):
            event = super().save(commit=False)
            event_start = event.start
            event_url = event.url




        if commit:
            event.save()
        return page
#model for events
@register_snippet
class Event(models.Model):
    api_url = models.CharField(max_length=255)
    event_start = models.DateTimeField(null=True)
    event_code = models.CharField(max_length=255, blank=True)
    event_url = models.CharField(max_length=255, blank=True)
    title   = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('user_event_id'),
        FieldPanel('api_url'),
        FieldPanel('event_start'),
        FieldPanel('event_code'),
        FieldPanel('title')


    ]

    base_form_class = EventForm

    def __str__(self):
        return self.title





# Let everyone know when a new page is published
def send_to_twitter(sender, **kwargs):
    instance = kwargs['instance']
    if instance.publish_to_twitter is True:
        print('\n url: ', instance.full_url, '\n title: ', instance.title, '\n relative url:', instance.url, '\n url path:', instance.url_path)
        print(instance.title)
        #setup the authentication
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        post_url = "http://isawebsite.com" + instance.url_path
        isa_tweet = "New post: \n" + instance.title + "\n " + post_url

        print(consumer_token)

        #tweet!
        api.update_status(isa_tweet)
    else:
        print('goodbye')

    return


# Register a receiver
page_published.connect(send_to_twitter, NewsPage)
