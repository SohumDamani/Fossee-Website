from django.db import models

from wagtail.models import Page
from layout.models import Layout
from streams import blocks
from wagtail import blocks as wagtailblocks

from wagtail.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel,InlinePanel


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super(HomePage,self).get_context(request)
        # I'm remaning page to point to layout page
        # Use self to access the page features
        context['layout'] = Layout.objects.get(slug='layout')
        return context

    max_count = 1

    content = StreamField([
        ('text',blocks.TitleAndContent(label='text')),
        ('images',blocks.ImageGalleryBlock()),
    ],null=True,collapsed=True)

    content_panels = Page.content_panels + [
        FieldPanel('content',heading="Page Body")
    ]

class FlexPage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super(FlexPage,self).get_context(request)
        context['layout'] = Layout.objects.get(slug='layout')
        return context

    content = StreamField([
        ('title',blocks.CharBlock()),
        ('text',blocks.CustomRichTextBlock(label='content')),
        ('images', blocks.ImageGalleryBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]




