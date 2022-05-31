from django.db import models

from wagtail.models import Page

from layout.models import Layout

class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super(HomePage,self).get_context(request)
        # I'm remaning page to point to layout page
        # Use self to access the page features
        context['page'] = Layout.objects.get(slug='layout')
        return context

