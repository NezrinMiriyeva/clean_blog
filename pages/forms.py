from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control"
    }))

    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        "class": "form-control"
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = ContactUs
        fields = ["name", "email",
                  "phone_number", "message"]

        labels = {
            "name": "Ad",
            "email" : "Elektron poct",
            "phone_number": "Telefon",
            "message": "mesaj"
        }
