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
