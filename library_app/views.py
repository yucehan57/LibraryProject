from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from . import models
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


class HomeView(generic.TemplateView):
    template_name = 'library_app/index.html'


class BookListView(generic.ListView):
    model = models.Book


class AuthorListView(generic.ListView):
    model = models.Author


class BookDetailView(generic.DetailView):
    model = models.Book

    # def query_set(self):


class AuthorDetailView(generic.DetailView):
    model = models.Author

    def query_set(self):
        """Get all the books of the author"""
        all_books = Book.objects.all()
        author_books = all_books.objects.filter(author=self.author_first_name)
        return author_books




def email_view(request):
    """view to check the validity of the contact form"""
    if request.method == 'GET':
        # create the empty form for the GET request
        form = ContactForm()
    else:
        # POST method
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['contact@libraryproject.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('success')
    return render(request, 'email.html', {'form': form})


def success_view(request):
    """View for sending a successful email"""
    return HttpResponse('Success! Thank you for your message')
