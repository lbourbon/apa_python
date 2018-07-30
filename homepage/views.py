from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name='home.html'

class Teste(TemplateView):
    template_name='teste.html'

class Precos(TemplateView):
    template_name='precos.html'

class About(TemplateView):
    template_name='about.html'

