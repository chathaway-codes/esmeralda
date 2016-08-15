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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from .views import HomePageView, render_page_pdf

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^.+.pdf$', render_page_pdf),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^double-king-pedro$', TemplateView.as_view(template_name='esmeralda/double_king.html'), name='double-king'),
    url(r'^lakehouse-paaarrrttayyyy-2016$', TemplateView.as_view(template_name='esmeralda/lakehouse-2016.html'), name='lakehouse-2016'),
    # For backward compatibility
    url(r'^weblog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
]
