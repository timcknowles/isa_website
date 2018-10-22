from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.search import index


# Create your models here.
class CourseIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class DateWithDescriptionBlock(blocks.StructBlock):
    date = blocks.DateBlock()
    description = blocks.CharBlock()

    class Meta:
        icon = 'date'


class CoursePage(Page):
    intro = models.CharField('one line summary', max_length=250)
    summary = RichTextField('full summary')
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(null=True,blank=True, help_text="for courses with consecutive dates")

    dates = StreamField([
        ('date_list', blocks.ListBlock(DateWithDescriptionBlock()))
    ], blank=True, help_text="for additional non consecutive dates")



    contact_details = StreamField([
        ('name', blocks.CharBlock(icon = 'user')),
        ('email', blocks.EmailBlock()),
        ('number', blocks.CharBlock()),

    ], blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('summary'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('summary', classname="full"),

        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('start_date', classname="full"),
                    FieldPanel('end_date', classname="full"),
                ]),
                StreamFieldPanel('dates', classname="full"),
            ],
            heading="Course Dates",
        ),




        StreamFieldPanel('contact_details'),



    ]
