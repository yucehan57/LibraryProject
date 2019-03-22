from django.shortcuts import render
from django.views import generic
from .models import Post


class BlogHomeView(generic.ListView):
    template_name = 'blog/blog.html'
    model = Post
    context_object_name = 'blogposts'

    """def get_queryset(self):"""
