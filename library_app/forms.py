from django import forms


class ContactForm(forms.Form):
    """Contact form for the user. This could be a feedback,
    a request, or an inquiery """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_mail(self):
        # send email using the self.cleaned_data
        pass

        
