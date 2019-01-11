from django.db import models
from django.db.models import Avg, Max, Min

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.search import index
from wagtail.core.models import Orderable, Page
from modelcluster.fields import ParentalKey
from wagtailgmaps.edit_handlers import MapFieldPanel
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.edit_handlers import ImageChooserPanel


# Create your models here.
class CourseIndexPage(Page):



    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super(CourseIndexPage, self).get_context(request)
        context['course_pages'] = CoursePage.objects.live().annotate(start_date=Min('related_dates__date')).order_by('start_date')
        # context['course_dates'] = CoursePage.objects.live()
        return context
    class Meta:
        verbose_name = "Courses & Conferences Index Page"

    parent_page_types = []



# class DateWithDescriptionBlock(blocks.StructBlock):
#     date = blocks.DateBlock()
#     description = blocks.CharBlock()
#
#     class Meta:
#         icon = 'date'

class RelatedLink(models.Model):
    title = models.CharField(max_length=255)
    link_external = models.URLField("External link", blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('link_external'),
    ]

    class Meta:
        abstract = True

class CoursePageRelatedLinks(Orderable, RelatedLink):
    page = ParentalKey('CoursePage', on_delete=models.CASCADE, related_name='related_links')


class RelatedDate(models.Model):
    date = models.DateField("Course Date", blank=True)
    description = models.CharField(max_length=255)

    panels = [
        FieldPanel('date'),
        FieldPanel('description'),
    ]

    class Meta:
        abstract = True






class CoursePageRelatedDates(Orderable, RelatedDate):
    page = ParentalKey('CoursePage', on_delete=models.CASCADE, related_name='related_dates')










class CoursePage(Page):

    parent_page_type = ["CourseIndexPage"]
    intro = models.CharField('one line summary', max_length=250)
    summary = RichTextField('full summary')
    # start_date = models.DateTimeField(blank=False)
    address_details = models.CharField('address details', max_length=250, blank=True)
    formatted_address = models.CharField(max_length=255)
    # latlng_address = models.CharField(max_length=255)

    course_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    course_flyer = StreamField([
        ('course_flyer', DocumentChooserBlock ()),

    ], blank=True)

    organiser_name = models.CharField('name', max_length=250, blank=True)
    organiser_email = models.EmailField('email', blank=True)
    organiser_number = models.CharField('number', max_length=250, blank=True)

    course_programme = StreamField([
        ('table', TableBlock()),

    ], blank=True)

    class Meta:
        verbose_name = "Courses & Conferences Page"
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('summary'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('summary', classname="full"),

        ImageChooserPanel('course_image'),
        InlinePanel('related_links', label="Course Links"),
        InlinePanel('related_dates', label="Course Dates"),
        StreamFieldPanel('course_programme'),
        StreamFieldPanel('course_flyer'),


        MultiFieldPanel(
        [
            FieldPanel('address_details', classname="full"),
            MapFieldPanel('formatted_address'),


        ],
        heading="Location",
        # classname="collapsible collapsed"
        ),

        MultiFieldPanel(
        [
            FieldPanel('organiser_name', classname="full"),
            FieldPanel('organiser_email', classname="full"),
            FieldPanel('organiser_number', classname="full"),


        ],
        heading="Organiser Details",
        # classname="collapsible collapsed"
        ),

        # MapFieldPanel('latlng_address', latlng=True),

    ]

    parent_page_types = ['CourseIndexPage']

    def get_context(self, request):
        context = super().get_context(request)
        relateddates = self.related_dates.order_by('date')
        #the [:1] returns the first result from the list e.g. the start date.
        context['relateddates'] = relateddates
        return context
