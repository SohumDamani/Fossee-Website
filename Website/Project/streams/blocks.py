from wagtail import blocks



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


class SidebarBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250,required=True)
    links = StreamBlock(
        [
            ('link',LinkBlock())
        ]
    )

    class Meta:
        template = "streams/self_block.html"
        icon = 'edit'
        label = 'Content'

class FooterBlock(blocks.StructBlock):
    title = CharBlock()
    content = blocks.RichTextBlock(label='Message')

    class Meta:
        template = "streams/self_block.html"
        icon='edit'
        label = 'Content'



