from django.views.generic import TemplateView

class IndexView(TemplateView): # Herdamos de TemplateView quando queremos apenas apresentar um template na tela
    template_name = 'index.html'