from forms import FichatesteForm
from .models import Fichateste
from django.views.generic.edit import CreateView
from django.shortcuts import redirect


class Fichosa(CreateView):
    template_name = 'fichosa.html'
    model = Fichateste
    fields = ['nome', 'data', 'bio']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = FichatesteForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.autor = request.user  # adiciona o autor da ficha antes de salvar
            form.save()
            return redirect('restrita')
