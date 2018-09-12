import customauth
from ficha.models import Ficha
from django.urls import reverse_lazy
from django.shortcuts import redirect
from forms import SignUpForm, ProfileForm
from django.db.models.functions import Lower
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, UpdateView


class Home(TemplateView):
    template_name = 'home.html'

    # redirect logged users to 'restrita'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('restrita')
        return super().dispatch(request, *args, **kwargs)


class Teste(LoginRequiredMixin, ListView):
    template_name = 'teste.html'
    model = Ficha


class Precos(TemplateView):
    template_name = 'precos.html'


class About(TemplateView):
    template_name = 'about.html'


class Contato(TemplateView):
    template_name = 'contato.html'


class Configuracoes(TemplateView):
    template_name = 'configuracoes.html'


class Ajuda(TemplateView):
    template_name = 'ajuda.html'


class Termos(TemplateView):
    template_name = 'termos.html'


class Privacidade(TemplateView):
    template_name = 'privacidade.html'


class Cadastro(FormView):
    form_class = SignUpForm
    template_name = 'cadastro.html'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        return redirect('profile_update', pk=self.request.user.profile.pk)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'profile_update.html'
    model = customauth.models.Profile
    fields = ['nome', 'crm', 'estado', 'telefone']
    success_url = reverse_lazy('restrita')

    def get_template_names(self):
        template_name = 'profile_update.html'
        referrer = str(self.request.META.get('HTTP_REFERER'))
        if (referrer.endswith('cadastro/')):
            template_name = 'profile.html'
        return template_name


class Restrita(LoginRequiredMixin, ListView):
    template_name = 'restrita.html'
    model = Ficha

    def order_query(self, query):
        ordem = str(self.request.GET.get('ordem'))
        if ordem == 'nome':
            query = query.order_by(Lower('nome'))
        elif ordem == '-nome':
            query = query.order_by(Lower('nome')).reverse()
        elif ordem == 'data':
            query = query.order_by('data')
        elif ordem == '-data':
            query = query.order_by('-data')
        return query

    def get_queryset(self):
        # pega apenas as fichas do usuário
        query = Ficha.objects.filter(user=self.request.user)
        # coloca no ordem solicitada
        if self.request.GET.get('ordem'):
            query = self.order_query(query)
        else:
            query = query.order_by('-data')

        search = self.request.GET.get('q')
        if search:
            query = query.filter(nome__icontains=search)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['busca'] = str(self.request.GET.get('q'))
        return context
