from django.contrib.auth.mixins import LoginRequiredMixin
from fichateste.models import Fichateste
from django.views.generic import TemplateView, ListView, DetailView


class Home(TemplateView):
    template_name='home.html'

class Teste(TemplateView):
    template_name='teste.html'

class Precos(TemplateView):
    template_name='precos.html'

class About(TemplateView):
    template_name='about.html'

class FichatesteDetail(DetailView):
    template_name='ficha_detail.html'
    model = Fichateste

class Restrita(LoginRequiredMixin, ListView):
    template_name='restrita.html'
    model = Fichateste

    def get_ordering(self):
        ordering = self.request.GET.get('ordem')
        return ordering
