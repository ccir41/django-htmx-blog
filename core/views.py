from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class PostView(TemplateView):
    template_name = 'post.html'