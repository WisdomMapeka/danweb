from django import forms

class Messages_from_client_form(forms.Form):
    name = forms.CharField(label="Name:", max_length=300)
    email = forms.EmailField(label="Email:", max_length=300)
    number = forms.CharField(label="Phone Number:", max_length=300)
    message = forms.CharField(label="Message", widget=forms.Textarea)
