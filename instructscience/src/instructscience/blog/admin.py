from django.contrib import admin
from . import models
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
# Register your models here.

@admin.register(models.BlogCategory)
class BlogCategoryAdmin(TreeAdmin, admin.ModelAdmin):
    list_display = ['category', 'created_on', 'updated_on',
                    'published']
    form = movenodeform_factory(models.BlogCategory)

@admin.register(models.BlogTopic)
class BlogTopicAdmin(TreeAdmin, admin.ModelAdmin):
    list_display = ['topic', 'blog_category', 'created_on', 'updated_on',
                    'published']
    form = movenodeform_factory(models.BlogTopic)

@admin.register(models.Blogs)
class BlogsAdmin(TreeAdmin, admin.ModelAdmin):
    list_display = ['blog_topic', 'blog_title', 'slug', 'content_published_date', 'created_on', 'updated_on',
                    'published']
    prepopulated_fields = {'slug': ('blog_title',), }
    form = movenodeform_factory(models.Blogs)

@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email_id', 'created_on', 'updated_on']
