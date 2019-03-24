from django.shortcuts import render, redirect, get_object_or_404
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
        context['historical_books'] = models.Book.objects.filter(
                                    genre__name__icontains='historical')[:5]
        return context


class BookListView(generic.ListView):
    model = models.Book
    paginate_by = 10



class AuthorListView(generic.ListView):
    model = models.Author
    paginate_by = 10

    def get_queryset(self):
        """List authors by their lastname order"""
        return models.Author.objects.order_by('last_name')


class BookDetailView(generic.DetailView):
    model = models.Book


class AuthorDetailView(generic.DetailView):
    model = models.Author
    
    # def get_context_data(self, **kwargs):
    #     """Display books from the same author"""
    #     context = super().get_context_data(**kwargs)
    #     from .models import Book
    #     context['author_books'] = Book.objects.filter(author_id=self.id)
    #     return context



class AddBookView(LoginRequiredMixin, generic.CreateView):

    model = models.Book
    fields = ('title', 'author', 'summary', 'isbn', 'genre')



class AddAuthorView(LoginRequiredMixin, generic.CreateView):
    model = models.Author
    fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death', 'bio')


class UpdateAuthorView(LoginRequiredMixin, generic.UpdateView):
    model = models.Author
    fields = ('bio',)
    template_name_suffix = '_update_form'


class GenreListView(generic.ListView):
    model = models.Genre


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
    return HttpResponse('Success! Thank you for your message. We will get back to you in 48 hours')
