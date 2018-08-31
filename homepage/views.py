from ficha.models import Ficha
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(TemplateView):
    template_name = 'home.html'


class Teste(TemplateView):
    template_name = 'teste.html'


class Precos(TemplateView):
    template_name = 'precos.html'


class About(TemplateView):
    template_name = 'about.html'


class Cadastro(FormView):
    form_class = UserCreationForm
    template_name = 'cadastro.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('restrita')


class Restrita(LoginRequiredMixin, ListView):
    template_name = 'restrita.html'
    model = Ficha

    def get_ordering(self):
        if self.request.GET.get('ordem'):
            return self.request.GET.get('ordem')
        return '-data'

