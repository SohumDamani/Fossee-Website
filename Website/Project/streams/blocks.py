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
        icon='edit'

class StreamBlock(blocks.StreamBlock):
    pass

class CharBlock(blocks.CharBlock):
    pass

class TitleAndContent(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250,required=True)
    content = blocks.RichTextBlock(required=True)

    class Meta:
        icon='edit'

class TitleAndLinks(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250,required=True)
    links = StreamBlock(
        [
            ('link',LinkBlock())
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






