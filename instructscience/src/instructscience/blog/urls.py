from django.urls import path, re_path
from django.conf.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve
app_name = 'blog'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('subscribe/', views.SubscriptionCreate, name='subscribe'),
    path('<slug:slug>/', views.BlogsDetailView.as_view(),
         name='blog_details'),

]
