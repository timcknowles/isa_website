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

#



class DateWithDescriptionBlock(blocks.StructBlock):
    date = blocks.DateBlock()
    description = blocks.CharBlock()

    class Meta:
        icon = 'date'

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
    intro = models.CharField('one line summary', max_length=250)
    summary = RichTextField('full summary')
    # start_date = models.DateTimeField(blank=False)
    formatted_address = models.CharField(max_length=255)
    latlng_address = models.CharField(max_length=255)


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
        InlinePanel('related_links', label="Related Links"),
        InlinePanel('related_dates', label="Related Dates"),
        StreamFieldPanel('contact_details'),
        MapFieldPanel('formatted_address'),
        # MapFieldPanel('latlng_address', latlng=True),

    ]

    def get_context(self, request):
        context = super().get_context(request)
        relateddates = self.related_dates.order_by('date')
        #the [:1] returns the first result from the list e.g. the start date.
        context['relateddates'] = relateddates
        return context
