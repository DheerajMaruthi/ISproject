from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from treebeard.mp_tree import MP_Node
from django.db.models import Sum
from django.conf import settings

# Create your models here.

class HomePageBanners(MP_Node):
    banner_title = models.CharField(
        _('Banner Title'), max_length=1000, null=True, blank=True,)
    desktop_banner_avatar = FilerImageField(related_name='desktop_banners',
                                            null=True,
                                            blank=True,
                                            on_delete=models.SET_NULL
                                            )
    mobile_banner_avatar = FilerImageField(related_name='mobile_banners',
                                           null=True,
                                           blank=True,
                                           on_delete=models.SET_NULL
                                           )
    description = RichTextField(null=True, blank=True)
    # #  basic log
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s' % (self.banner_title)

    class Meta:
        verbose_name = 'Home Page Banners'
        verbose_name_plural = 'Home Page Banners'


class Expertise(MP_Node):
    title = models.CharField(
        _('Title'), max_length=1000, null=True, blank=True,)
    logo = FilerImageField(related_name='logo',
                                            null=True,
                                            blank=True,
                                            on_delete=models.SET_NULL
                                            )

    description = RichTextField(null=True, blank=True)
    # #  basic log
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Expertise'
        verbose_name_plural = 'Expertise'
