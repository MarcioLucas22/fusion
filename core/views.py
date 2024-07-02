from typing import Any
from django.views.generic import TemplateView
from .models import Servico, Funcionario, Funcionalidade

class IndexView(TemplateView): # Herdamos de TemplateView quando queremos apenas apresentar um template na tela
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        context['funcionalidades'] = Funcionalidade.objects.all()

        return context
    