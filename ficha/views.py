import re
from ficha.models import Ficha
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class FichaNew(LoginRequiredMixin, CreateView):
    template_name = 'ficha.html'
    model = Ficha
    fields = '__all__'
    success_url = '/'

    def is_mobile(self):
        """Return True if the request comes from a mobile device."""

        MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)", re.IGNORECASE)
        return MOBILE_AGENT_RE.match(self.request.META['HTTP_USER_AGENT'])

    def get_template_names(self):
        template_name = 'ficha.html'
        if self.is_mobile():
            template_name = 'ficha_mobile.html'
        return template_name

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        if self.request.POST['fim'] == 'IMPRIMIR':
            print("-> COMANDO: IMPRIMIR <-")
            return redirect('ficha_print', pk=form.pk)
        return redirect('restrita')

    def form_invalid(self, form):
        print('Errrrou:', form.errors)
        return super().form_invalid(form)

class FichaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'ficha.html'
    model = Ficha
    fields = '__all__'
    success_url = reverse_lazy('restrita')


    def has_permission(self):
        return self.request.user == Ficha.objects.get(pk=self.kwargs['pk']).user

    def is_mobile(self):
        """Return True if the request comes from a mobile device."""

        MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)", re.IGNORECASE)
        return MOBILE_AGENT_RE.match(self.request.META['HTTP_USER_AGENT'])

    def get_template_names(self):
        template_name = 'ficha.html'
        if self.is_mobile():
            template_name = 'ficha_mobile.html'
        return template_name

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('restrita')

    def form_invalid(self, form):
        print('Errrrou:', form.errors)
        return super().form_invalid(form)


class FichaPrint(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'ficha_print.html'
    model = Ficha
    fields = '__all__'
    success_url = reverse_lazy('restrita')

    def has_permission(self):
        return self.request.user == Ficha.objects.get(pk=self.kwargs['pk']).user



class FichaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'ficha_delete.html'
    model = Ficha
    success_url = reverse_lazy('restrita')

    def has_permission(self):
        return self.request.user == Ficha.objects.get(pk=self.kwargs['pk']).user

class Tcle(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'tcle.html'
    model = Ficha
    fields = '__all__'
    success_url = reverse_lazy('restrita')

    def has_permission(self):
        return self.request.user == Ficha.objects.get(pk=self.kwargs['pk']).user

class Orcamento(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'orcamento.html'
    model = Ficha
    fields = '__all__'
    success_url = reverse_lazy('restrita')

    def has_permission(self):
        return self.request.user == Ficha.objects.get(pk=self.kwargs['pk']).user
