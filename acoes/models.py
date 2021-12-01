from django.db import models

class Filmes(models.Model):
    nome_do_filme = models.CharField(max_length=200)
    autor_do_filme = models.CharField(max_length=200)
    data_publicada_do_filme = models.DateTimeField("Publicado em")
    genero_do_filme = models.CharField(max_length=100)
    classificacao_do_filme = models.SmallIntegerField()
    elenco_do_filme = models.CharField(max_length=5000)

    def __str__(self):
        return self.nome_do_filme

class Series(models.Model):
    nome_da_serie = models.CharField(max_length=200)
    autor_da_serie = models.CharField(max_length=200)
    data_publicada_da_serie = models.DateTimeField("Publicado em")
    genero_da_serie = models.CharField(max_length=100)
    classificacao_da_serie = models.SmallIntegerField()
    elenco_da_serie = models.CharField(max_length=5000)

    def __str__(self):
        return self.nome_da_serie

class HQs(models.Model):
    nome_da_hq = models.CharField(max_length=200)
    data_publicada_da_hq = models.DateTimeField("Publicado em")
    genero_da_hq = models.CharField(max_length=100)
    numero_da_hq = models.SmallIntegerField()
    editora_da_hq = models.CharField(max_length=200)
    personagens_da_hq = models.CharField(max_length=5000)
    quantidade_de_paginas = models.SmallIntegerField()

    def __str__(self):
        return self.nome_da_hq


class Noticias(models.Model):
    foto_da_noticia = models.ImageField(blank=True)
    titulo_da_noticia = models.TextField(blank=True)
    noticias = models.TextField()

    def __str__(self):
        return self.titulo_da_noticia


class Opinioes(models.Model):
    nome_da_obra = models.CharField(max_length=200)
    opiniao = models.CharField(max_length=9999)

    def __str__(self):
        return self.nome_da_obra

