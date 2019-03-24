from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class PostHomeView(generic.ListView):
    model = Post
    context_object_name = 'blog_posts'
    paginate_by = 5
    """def get_queryset(self):"""


class PostDetailView(generic.DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ('title', 'content', 'category', 'tags')
    context_object_name = 'blogpost'
    template_name = 'blog/post_update_form.html'
