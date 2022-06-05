from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock



class StreamBlock(blocks.StreamBlock):
    class Meta:
        icon = 'edit'

class CharBlock(blocks.CharBlock):
    pass
    class Meta:
        icon = 'edit'

class LinkBlock(blocks.StructBlock):
    link = blocks.RichTextBlock(features=['link'], required=True)
    visible = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        template="streams/internal_link_block.html"
        icon = 'link'
        label = 'Link'

class ExternalLinkBlock(blocks.StructBlock):
    placeholder = CharBlock(max_length=255)
    link = blocks.URLBlock()
    visible = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        template = 'streams/external_link_block.html'
        icon = 'link'

class CustomRichTextBlock(blocks.RichTextBlock):
    def __init__(self,**kwargs,):
        super().__init__(**kwargs)
        self.features = ['h1','h2','h3','h4','h5','h6',
                    'bold','italic','ol','ul','hr',
                    'link','document-link','embed','code',
                    'blockquote']

    class Meta:
        template = 'streams/self_block.html'

class Gallery(blocks.ListBlock):
    pass

class TitleAndContent(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250,required=False)
    type = blocks.ChoiceBlock(choices=[
        ('accordion','Accordion'),
        ('row-col','Row and Column'),
        ('normal','Normal'),
    ])
    content = blocks.RichTextBlock(required=True)
    # data = blocks.StreamBlock([
    #     ('content',blocks.RichTextBlock())
    # ],min=1,label="Content")

    class Meta:
        template = 'streams/title_and_content.html'
        icon='edit'

class TitleAndLinks(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250,required=True)
    links = StreamBlock(
        [
            ('link',LinkBlock(label='Internal Link')),
            ('ext_link',ExternalLinkBlock(label='External Link'))
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

class ImageGalleryBlock(blocks.StructBlock):
    html = blocks.RawHTMLBlock(required=False)
    heading = blocks.StructBlock([
        ('title',CharBlock(required=False)),
        ('visible',blocks.BooleanBlock(default=False))
        ],heading='title',form_classname = 'person-block struct-block'
)
    col = blocks.IntegerBlock(required=True,
                              default=3,
                              label='Columns',
                              help_text="no. of images in one row")
    images = blocks.ListBlock(ImageBlock())


    class Meta:
        template = 'streams/img_gallery.html'
        icon='image'






