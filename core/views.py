from typing import Any
from django.http import HttpResponse
from django.views.generic import FormView
from .models import Servico, Funcionario, Funcionalidade
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        context['funcionalidades'] = Funcionalidade.objects.all()

        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso')

        return super(IndexView, self).form_valid(form)
    
    def form_invalid(self, form: Any) -> HttpResponse:
        messages.error(self.request, 'Erro ao enviar email')
        return super(IndexView, self).form_invalid(form)