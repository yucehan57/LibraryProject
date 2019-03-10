from django import forms

class ContactForm(forms.Form):
    """Contact form for the user. This could be a feedback,
    a request, or an inquiery """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)



class AddBookForm(forms.Form):
    """To add a book to the Library"""
