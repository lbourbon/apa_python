from fichateste.models import Fichateste
from django.forms import ModelForm

class FichatesteForm(ModelForm):
    class Meta:
        model = Fichateste
        exclude = ['autor']
