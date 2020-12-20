import hashlib
import json
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from treebeard.mp_tree import MP_Node
from ckeditor.fields import RichTextField

# Create your models here.

class BlogCategory(MP_Node):
    category = models.CharField(_('Category'), max_length=100)
    created_on = models.DateTimeField(_('Created Date'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated Date'), auto_now=True)
    published = models.BooleanField(_('Published on'), default=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'


class BlogTopic(MP_Node):
    blog_category = models.ForeignKey(BlogCategory,
                                      verbose_name=_('Blog Category'), null=True, blank=True, on_delete=models.CASCADE, related_name="blog_category")
    topic = models.CharField(_('Topic'), max_length=100)
    created_on = models.DateTimeField(_('Created Date'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated Date'), auto_now=True)
    published = models.BooleanField(_('Published on'), default=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Blog Topic'
        verbose_name_plural = 'Blog Topics'


class Blogs(MP_Node):
    blog_topic = models.ForeignKey(BlogTopic,
                                         verbose_name=_('Blog Topic'), null=True, blank=True, on_delete=models.CASCADE, related_name="blog_topic")
    blog_title = models.CharField(
        _('Blog Title'), max_length=1000, null=True, blank=True,)
    slug = models.SlugField(max_length=500, blank=True, null=True)
    blog_short_description = models.TextField()
    blog_content = RichTextField(null=True, blank=True)
    content_published_date = models.DateTimeField(blank=False, null=False)
    blog_image = FilerImageField(related_name='blog_image',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL
                                    )
    blog_big_image = FilerImageField(related_name='blog_big_image',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL
                                    )
    blog_author = models.CharField(
        _('Blog Author'), max_length=1000, null=True, blank=True,)
    search_friendly = models.TextField(
        _('Search Friendly'), null=True, blank=True)
    # #  basic log
    featured = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return '%s' % (self.blog_title)

    class Meta:
        verbose_name = ' Blog'
        verbose_name_plural = 'Blogs'


class Subscription(models.Model):
    email_id = models.EmailField(
        _('Email'), max_length=100)
    hash = models.TextField(unique=True)
    notification = models.CharField(
        _('Notification'), blank=True, null=True, max_length=50)
    # basic log
    subscribed = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.email_id)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Email Subscriptions'

    def save(self, *args, **kwargs):
        if self.email_id:
            try:
                secret = settings.SECRET_KEY.encode('utf-8')
                hasher = (self.email_id).encode('utf-8')
                self.hash = hashlib.md5(hasher + secret).hexdigest()
            except Exception as e:
                pass
        super(Subscription, self).save(*args, **kwargs)

    def unsubscribe(self, email):
        if self.email == email:
            self.subscribed = False
            self.save()
