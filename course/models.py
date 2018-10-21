from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.search import index


# Create your models here.
class CourseIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class CoursePage(Page):
    intro = models.CharField('one line summary', max_length=250)
    summary = RichTextField('full summary', max_length=250)
    start_date = models.DateTimeField("course start")
    end_date = models.DateTimeField("course end")



    dates = StreamField([
         ('date_list', blocks.ListBlock(blocks.DateBlock(required=False))),
    ], blank=True)



    links = StreamField([
        ('url', blocks.URLBlock()),

    ], blank=True)



    documents = StreamField([
        ('document', DocumentChooserBlock()),

    ], blank=True)

    contact_details = StreamField([
        ('name', blocks.CharBlock()),
        ('email', blocks.EmailBlock()),
        ('number', blocks.CharBlock()),

    ], blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('summary'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro',),
        FieldPanel('summary'),
        StreamFieldPanel('dates'),
        FieldRowPanel([
            FieldPanel('start_date'),
            FieldPanel('end_date'),
            # StreamFieldPanel('date_list'),
        ]),
        StreamFieldPanel('links'),
        StreamFieldPanel('documents'),
        StreamFieldPanel('contact_details'),



    ]
