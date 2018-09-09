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

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('restrita')


class FichaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'ficha_update.html'
    model = Ficha
    fields = '__all__'
    success_url = reverse_lazy('restrita')

    def has_permission(self):
        return self.request.user == Ficha.objects.get(pk=self.kwargs['pk']).user

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('restrita')


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
