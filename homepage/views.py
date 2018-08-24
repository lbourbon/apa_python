from django.contrib.auth.mixins import LoginRequiredMixin
from fichateste.models import Fichateste
from django.views.generic import TemplateView, ListView


class Home(TemplateView):
    template_name='home.html'

class Teste(TemplateView):
    template_name='teste.html'

class Precos(TemplateView):
    template_name='precos.html'

class About(TemplateView):
    template_name='about.html'

class Restrita(LoginRequiredMixin, ListView):
    template_name='restrita.html'
    model = Fichateste
    ordering = ['nome']