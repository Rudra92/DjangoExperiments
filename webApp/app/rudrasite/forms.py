from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=500, required=True)
