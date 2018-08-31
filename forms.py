from fichateste.models import Fichateste
from django.forms import ModelForm
from ficha.models import Ficha


class FichaForm(ModelForm):
    class Meta:
        model = Ficha
        exclude = ['user',]


class FichatesteForm(ModelForm):
    class Meta:
        model = Fichateste
        exclude = ['autor']


