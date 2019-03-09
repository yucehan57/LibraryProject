from django.shortcuts import render
from django.views import generic
from . import models

class HomeView(generic.TemplateView):
    template_name = 'library_app/index.html'


class BookListView(generic.ListView):
    model = models.Book


class AuthorListView(generic.ListView):
    model = models.Author
    
