from django import forms
from ficha.models import Ficha
from homepage.models import Espera
from django.forms import ModelForm
from customauth.models import MyUser, Profile
from django.contrib.auth.forms import UserCreationForm


class FichaForm(ModelForm):
    data = forms.DateField(input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%d/%m/%Y', '%d-%m-%Y'])

    class Meta:
        model = Ficha
        exclude = ['user', ]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')


class EsperaForm(ModelForm):

    class Meta:
        model = Espera
        fields = ('nome', 'email', 'fone')


class ProfileForm(forms.ModelForm):
    nome = forms.CharField(label="Nome Completo")
    telefone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'DDD + Número. Apenas dígitos.'}))
    class Meta:
        model = Profile
        fields = ('nome', 'crm', 'estado', 'telefone')



