from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import forms
from . import models

from django.contrib.auth.decorators import login_required


class SignUpView(generic.CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
