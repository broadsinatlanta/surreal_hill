from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import (FieldPanel, StreamFieldPanel,
                                         FieldRowPanel, InlinePanel,
                                         MultiFieldPanel)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


class HomePage(Page):
    tagline = RichTextField(blank=True)
    body = StreamField([
        ('welcome', blocks.RichTextBlock()),
        ('about', blocks.RichTextBlock()),
        ('photo', ImageChooserBlock()),
        ])

    content_panels = Page.content_panels + [
        FieldPanel('tagline', classname='full'),
        StreamFieldPanel('body')
    ]


class ContactFormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]
