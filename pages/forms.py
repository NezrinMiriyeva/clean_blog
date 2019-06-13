from django import forms
from .models import ContactUs
from .models import Articles
from django.contrib.auth import get_user_model

User = get_user_model()


# class Articleform(forms.ModelForm):
#
#     class Meta:
#         model = Articles
#         fields = ["name","sub_title","content","author"]

class RegistrationUserForms(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name",
                  "email", "username", "password"]

        labels = {
            "first_name": "Ad",
            "last_name": "Soyad",
            "email" : "Elektron poct",
            "username": "Istifadeci adi",
            "password": "Sifre"
        }

        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': 'Ad'})
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control"
    }))


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
