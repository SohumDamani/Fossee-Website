from django.db import models

from layout.models import Layout

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel,InlinePanel

# class TestPage(Page):
#
#     def get_context(self, request, *args, **kwargs):
#         context = super(TestPage, self).get_context(request)
#         context['page']=Layout.objects.get(slug='layout')
#         return context
#
#     body = models.CharField(max_length=255,null=True)
#
#     content_panels = Page.content_panels + [
#         FieldPanel('body')
#     ]


# Create your models here.
