from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class LinkBlock(blocks.StructBlock):
    link = blocks.RichTextBlock(features=['link'], required=True)
    visible = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        template="streams/self_block.html"
        icon = 'link'
        label = 'Link'

class Gallery(blocks.ListBlock):

    class Meta:
        template = 'streams/gallery.html'
        icon='edit'

class StreamBlock(blocks.StreamBlock):
    class Meta:
        icon = 'edit'

class CharBlock(blocks.CharBlock):
    pass
    class Meta:
        icon = 'edit'

class CustomRichTextBlock(blocks.RichTextBlock):
    def __init__(self,**kwargs,):
        super().__init__(**kwargs)
        self.features = ['h1','h2','h3','h4','h5','h6',
                    'bold','italic','ol','ul','hr',
                    'link','document-link','embed','code',
                    'blockquote']

    class Meta:
        template = 'streams/self_block.html'

class ExternalLinkBlock(blocks.StructBlock):
    placeholder = CharBlock(max_length=255)
    link = blocks.URLBlock()

    class Meta:
        icon = 'link'
        template = 'streams/self_block.html'

class TitleAndContent(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250,required=True)
    content = blocks.RichTextBlock(required=True)

    class Meta:
        icon='edit'

class TitleAndLinks(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250,required=True)
    links = StreamBlock(
        [
            ('link',LinkBlock()),
            ('ext_link',ExternalLinkBlock())
        ],collapsed=True
    )

    class Meta:
        template = "streams/self_block.html"
        icon = 'edit'
        label = 'Content'

class ImageBlock(blocks.StructBlock):
    title = CharBlock(max_length=255,
                      help_text="Add only if you want to display it with the image",
                      required=False)
    img = ImageChooserBlock(required=True)
    img_link = blocks.URLBlock(required=False,
                               help_text="Hyperlink the image to given url")

    class Meta:
        template = 'streams/image_block.html'
        icon = 'image'







