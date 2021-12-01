from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('filmes/', views.FilmeView.as_view(), name='filmes'),
    path('series/', views.SerieView.as_view(), name='series'),
    path('quadrinhos/', views.HqView.as_view(), name='quadrinhos'),
    path('noticias/',  views.NoticiasView.as_view(), name='noticias'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]