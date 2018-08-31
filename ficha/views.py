from forms import FichaForm
from ficha.models import Ficha
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class FichaNew(CreateView):
    template_name = 'ficha.html'
    model = Ficha
    fields = '__all__'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = FichaForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.autor = request.user  # adiciona o autor da ficha antes de salvar
            form.save()
            return redirect('restrita')


class FichaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'ficha_update.html'
    model = Ficha
    fields = '__all__'
    success_url = reverse_lazy('restrita')


class FichaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'ficha_delete.html'
    model = Ficha
    success_url = reverse_lazy('restrita')

#
# @login_required
# def ficha(request):
#     form = FichaForm(request.POST or None)
#     if form.is_valid():
#         form = form.save(commit=False)
#         form.user = request.user  # adiciona o autor da ficha antes de salvar
#         form.save()
#         return redirect('restrita')
#
#     return render(request, 'ficha.html', {'form': form})
#
# @login_required
# def abrir_ficha(request, id):
#     paciente = get_object_or_404(Ficha, pk=id)
#     form = FichaForm(request.POST or None, instance=paciente)
#     if form.is_valid():
#         form = form.save(commit=False)
#         form.user = request.user  # adiciona o autor da ficha antes de salvar
#         form.save()
#         return redirect('restrita')
#
#     return render(request, 'ler_ficha.html', {'form': form})
#
# @login_required
# def apagar_ficha(request, id):
#     paciente = get_object_or_404(Ficha, pk=id)
#     if request.method == 'POST':
#         paciente.delete()
#         return redirect('restrita')
#
#     return render(request, 'apagar_ficha.html', {'paciente': paciente})
#
# @login_required
# def termo(request, id):
#     paciente = get_object_or_404(Ficha, pk=id)
#     form = FichaForm(request.POST or None, instance=paciente)
#     return render (request, 'termo.html', {'form': form})
