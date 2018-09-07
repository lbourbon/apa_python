from django import forms
from ficha.models import Ficha
from django.forms import ModelForm
from customauth.choices import ESTADOS_CHOICES
from customauth.models import MyUser, Profile
from django.contrib.auth.forms import UserCreationForm


class FichaForm(ModelForm):
    class Meta:
        model = Ficha
        exclude = ['user', ]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    nome = forms.CharField(label="Nome Completo")
    telefone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'DDD + Número. Apenas dígitos.'}))
    class Meta:
        model = Profile
        fields = ('nome', 'crm', 'estado', 'telefone')
