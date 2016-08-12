from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import BlogPost

# Create your views here.
class BlogPostDetailView(DetailView):
    model = BlogPost
class BlogPostListView(ListView):
    model = BlogPost
