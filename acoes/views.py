from django.views import generic
from .models import Filmes,Series,HQs, Noticias

class IndexView(generic.ListView):
    model = Filmes
    template_name = 'acao/index.html'


class FilmeView(generic.ListView):
    model = Filmes
    template_name = 'acao/filmes.html'
    context_object_name = 'lista_filmes'
    def get_queryset(self):
        return Filmes.objects.order_by('-nome_do_filme')

class SerieView(generic.ListView):
    model = Series
    template_name = 'acao/series.html'
    context_object_name = 'lista_de_serie'
    def get_queryset(self):
        return Series.objects.order_by('-nome_da_serie')

class HqView(generic.ListView):
    model = HQs
    template_name = 'acao/hqs.html'
    context_object_name = 'lista_de_hq'
    def get_queryset(self):
        return HQs.objects.order_by('-nome_da_hq')

class NoticiasView(generic.ListView):
    model = Noticias
    template_name = 'acao/noticias.html'
    context_object_name = 'listas_de_noticia'
    def get_queryset(self):
        return Noticias.objects.order_by('-noticias')

class DetailView(generic.DetailView):
    model = Filmes
    template_name = 'acao/detail.html'
    context_object_name = 'question'

class ResultsView(generic.DetailView):
    model = Filmes
    template_name = 'acao/results.html'
    context_object_name = 'question'
