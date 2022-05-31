from django.db import models
from django import forms

from streams import blocks

from wagtail.models import Page,Orderable
from modelcluster.fields import ParentalManyToManyField
from modelcluster.fields import ParentalKey


from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

@register_snippet
class Navbar(models.Model):
    title = models.CharField(primary_key=True,max_length=255)
    logo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.CASCADE, related_name='+'
    )
    links = StreamField([
        ('navs',blocks.LinkBlock())
    ],null=True,blank=True)

    panels = [FieldPanel('title'),
              ImageChooserPanel('logo'),
              FieldPanel('links',heading='Nav Links',classname='collapsible')]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Navbar"
        verbose_name_plural = "Navbars"

@register_snippet
class Sidebar(models.Model):
    title = models.CharField(primary_key=True,max_length=255)
    sidebar = StreamField(
        [
            ('sidebar',blocks.SidebarBlock())
        ],null=True,blank=True)
    panels = [FieldPanel('title'),
              FieldPanel('sidebar')]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sidebar"
        verbose_name_plural = "Sidebars"

@register_snippet
class Footer(models.Model):
    title = models.CharField(primary_key=True,max_length=255)
    footer = StreamField(
        [
            ('contents', blocks.FooterBlock()),
            ('extlinks',blocks.SidebarBlock(label='External Links',icon='link'))
        ],null=True,blank=True)

    panels = [FieldPanel('title'),
              FieldPanel('footer')]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footers"

@register_snippet
class Banner(models.Model):
    title = models.CharField(primary_key=True,max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [FieldPanel('title'),
              FieldPanel('banner')]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"




