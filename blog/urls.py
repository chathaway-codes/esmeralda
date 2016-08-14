"""esmeralda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .views import BlogPostDetailView, BlogPostListView

urlpatterns = [
    url(r'^(?P<slug>[^/]+)$', BlogPostDetailView.as_view(), name='blog-post-detail'),
    url(r'^$', BlogPostListView.as_view(), name='blog-list'),

    # Compatibility URL's
    url(r'^\d{4}/\d{2}/\d{2}/(?P<slug>[^/]+)/$', BlogPostDetailView.as_view()),
]
