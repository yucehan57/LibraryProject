from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from . import models
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView


class HomeView(generic.TemplateView):

    template_name = 'library_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = models.Book.objects.all().count()
        context['num_instances'] = models.BookInstance.objects.all().count()
        context['num_authors'] = models.Author.objects.all().count()
        return context



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


class AddBookView(LoginRequiredMixin, generic.CreateView):

    model = models.Book
    fields = ('title', 'author', 'summary', 'isbn', 'genre')



class AddAuthorView(LoginRequiredMixin, generic.CreateView):
    model = models.Author
    fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death', 'bio')



class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_mail()
        return super().form_valid(form)



# def email_view(request):
#     """view to check the validity of the contact form"""
#     if request.method == 'GET':
#         # create the empty form for the GET request
#         form = ContactForm()
#     else:
#         # POST method
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['contact@libraryproject.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found')
#             return redirect('success')
#     return render(request, 'contact.html', {'form': form})


def success_view(request):
    """View for sending a successful email"""
    return HttpResponse('Success! Thank you for your message')

def success_book_added_view(request):
    """view for adding a book successfully"""
    return HttpResponse('Book successfully added.')
    #
    # FINISH FUNCTIONALITY
