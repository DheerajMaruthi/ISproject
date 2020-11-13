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
from django.http import HttpResponseRedirect
from django.urls import reverse
from el_pagination.views import AjaxListView
from django.db.models import Q
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class Index(AjaxListView):
    template_name = 'blog/blogs.html'
    model = models.Blogs
    context_object_name = "blogs"
    page_template = 'blog/entry_list_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['recent'] = models.Blogs.objects.filter(
            published=True).order_by('content_published_date')
        context['feature'] = models.Blogs.objects.filter(
            published=True,featured=True)
        context['category'] = models.BlogCategory.objects.filter(
            published=True)
        context['topic'] = models.BlogTopic.objects.filter(
            published=True)
        return context

class BlogsDetailView(generic.TemplateView):
    template_name = 'blog/blogdetails.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogsDetailView,
                        self).get_context_data(*args, **kwargs)
        obj = self.kwargs['slug']
        context['recent'] = models.Blogs.objects.filter(
            published=True).order_by('content_published_date')
        context['blog_object'] = models.Blogs.objects.get(
        slug=obj)
        return context


def SubscriptionCreate(request):
    if request.method == 'POST':
        email = request.POST.get('email_id')
        notification = request.POST.get('notification')
        if email == '':
            message = 'Email cannot be empty'
            return HttpResponse(json.dumps({'message': message}), content_type='application/json')
        else:
            try:
                validate_email(email)
            except:
                message = 'Please enter a valid email address'
                return HttpResponse(json.dumps({'message': message}), content_type='application/json')

            if models.Subscription.objects.filter(email_id=email).exists():
                models.Subscription.objects.filter(
                    email_id=email).update(notification=notification)
                message = 'You are already subscribed to our Newsletter and your notification choice updated'
            else:
                try:
                    m = models.Subscription.objects.create(email_id=email, hash=hash,
                                                               notification=notification,
                                                               )
                except Exception as e:
                    print(e)
                    pass
                m.save()
                # subject2 = "A New Subscription"
                # from_email = "covid19@embassyofficeparks.com"
                # admin_email = "covid19@embassyofficeparks.com"
                #
                # template_object_admin = render_to_string(
                #     'subscribe_admin.html', {"email":email, 'last_name':last_name, "notification": notification})
                # send_mail(subject=subject2, template_object=template_object_admin,
                #   from_email=from_email, to=[admin_email], resume=None,
                #   fail_silently=False)

                message = "Thank you for Subscribing to our Newsletter"

            ctx = {'message': message}
        return HttpResponse(json.dumps(ctx), content_type='application/json')


def Confirm(request, email, hash):
    return render(request, "confirm.html")


def Unsubscribe(request, email, hash):
    for row in models.Subscription.objects.all():
        if models.Subscription.objects.filter(id=row.id).filter(email_id__icontains=email).filter(hash__icontains=hash):
            row.unsubscribe(email)
    return render(request, "unsubcribe.html")


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = models.Blogs.objects.filter(
            search_friendly__icontains=q)
        results = []
        # print(q)
        # print(search_qs)
        for r in search_qs:
            results.append(r.article_title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def Blog_search(request, slug=None):
    if request.method == 'GET':
        q = request.GET.get('txtSearch')
        if q:
            try:
                results = models.Blogs.objects.get(
                        article_title=q, published=1)
                blogs = models.Blogs.objects.filter(published=1)
                social_feeds_obj = models.SocialFeeds.objects.filter(
                        published=True)
                return render(request, 'home/blogdetails.html', {'blog_object': results, 'articles': articles,'social_feeds_obj':social_feeds_obj})
            except Exception as e:
                results = models.Blogs.objects.filter(
                        Q(search_friendly__icontains=q)
                        | Q(article_title__icontains=q), published=1)
                return render(request, 'home/search_results.html', {'blogs': results})
