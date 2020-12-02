import requests
from django.views import generic
from . import models
import json
import hashlib
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.core.mail import EmailMessage
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.validators import validate_email
from django.db.models import Q



class HomeView(generic.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['banners'] = models.HomePageBanners.objects.filter(
            published=True)
        context['expertise'] = models.Expertise.objects.filter(
            published=True)
        return context

class WoiView(generic.TemplateView):
    template_name = 'home/inspire.html'

    def get_search_object(self):
        video_search_list = models.Video.objects.filter(
            published=1).order_by('-content_published_date')
        book_search_list = models.Book.objects.filter(
            published=1).order_by('-content_published_date')
        # gallery_search_list = models.Gallery.objects.filter(
        #     published=1).order_by('-content_published_date')
        video_year = self.request.GET.get('video_year')
        book_year = self.request.GET.get('book_year')
        # gallery_year = self.request.GET.get('gallery_year')
        if video_year:
            video_search_list = models.Video.objects.filter(content_published_date__year=video_year, published=1).order_by('-content_published_date')

        if book_year:
            book_search_list = models.Book.objects.filter(
                Q(content_published_date__year=book_year), published=1).order_by('-content_published_date')

        # if gallery_year:
        #     search_list = models.Gallery.objects.filter(
        #         Q(content_published_date__month=Month), published=1).order_by('-content_published_date')

        return video_search_list,book_search_list

    def get_context_data(self, *args, **kwargs):
        context = super(WoiView,
                        self).get_context_data(*args, **kwargs)
        video_search_list,book_search_list = self.get_search_object()
        context['video_search_list'] = video_search_list
        context['book_search_list'] = book_search_list
        # context['gallery_search_list'] = gallery_search_list
        context['vid_year'] = models.Video.objects.values('content_published_date__year').distinct().order_by('-content_published_date__year')
        context['b_year'] = models.Book.objects.values('content_published_date__year').distinct().order_by('-content_published_date__year')
        context['gallery_obj'] = models.Gallery.objects.filter(
            published=1).order_by('-content_published_date')
        return context
