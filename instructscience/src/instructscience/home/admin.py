import requests
from django.contrib import admin
from . import models
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from django.contrib.sites.models import Site
from django.http import HttpResponse
from datetime import datetime
from import_export.admin import ImportExportModelAdmin


@admin.register(models.HomePageBanners)
class HomePageBannersAdmin(TreeAdmin, admin.ModelAdmin):

    list_display = ['banner_title',
                    'desktop_banner_avatar', 'mobile_banner_avatar', 'published', 'created_on', 'updated_on'
                    ]

    form = movenodeform_factory(models.HomePageBanners)


@admin.register(models.Expertise)
class ExpertiseAdmin(TreeAdmin, admin.ModelAdmin):
    list_display = ['title', 'logo', 'description', 'created_on', 'updated_on',
                    'published']
    form = movenodeform_factory(models.Expertise)
