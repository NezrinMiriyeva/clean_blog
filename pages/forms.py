from django import forms
from .models import ContactUs
from .models import Articles
from django.contrib.auth import get_user_model

User = get_user_model()


class Articleform(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ["name","background_image","sub_title","content"]

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Ad'}),
            "sub_title": forms.TextInput(attrs={'placeholder': 'Basliq'}),
            "content": forms.Textarea(attrs={'placeholder': 'Text'}),
        }

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
            "first_name": forms.TextInput(attrs={'placeholder': 'Ad'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Soyad'}),
            "email": forms.TextInput(attrs={'placeholder': 'Elektron poct'}),
            "username": forms.TextInput(attrs={'placeholder': 'Istifadeci adi'}),
            "password": forms.PasswordInput(attrs={'placeholder': 'Sifre'})

        }

    def __init__(self, *args, **kwargs):
        super(RegistrationUserForms, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['username'].required = True
        self.fields['password'].required = True



class LoginForm(forms.Form):
    username = forms.CharField(label="Istifadeci adi",widget=forms.TextInput(attrs={
        "class": "form-control",
        'placeholder': 'Ad'
    }))
    password = forms.CharField(label="Sifre",widget=forms.PasswordInput(attrs={
        "class": "form-control",
        'placeholder': 'Sifre'
    }))

    # labels = {
    #     "username": "Istifadeci adi",
    #     "password": "Sifre"
    # }

    # widgets = {
    #     "username": forms.TextInput(attrs={'placeholder': 'Istifadeci adi'}),
    #     "password": forms.PasswordInput(attrs={'placeholder': 'Sifre'})
    #
    # }


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


class UserSettingsForm(forms.ModelForm):
    password = forms.CharField(label="Sifre",widget=forms.PasswordInput(attrs={
        'placeholder': 'Sifre'
    }))
    image = forms.ImageField()

    class Meta:
        model = User
        fields = [
            "first_name", "last_name",
            "email",
        ]
