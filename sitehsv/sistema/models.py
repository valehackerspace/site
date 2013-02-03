# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (1, u'Proposta'),
    (2, u'Em Andamento'),
    (2, u'Concluído'),
    (2, u'Abandonado'),
    )


class Projeto(models.Model):
    nome = models.CharField(u'Projeto', max_length=50, blank=False, null=False)
    descricao = models.TextField(u'Descrição', blank=False, null=False)
    inicio = models.DateField(u'Data de Início', blank=True, null=True)
    previsao_termino = models.DateField(u'Previsão de Término', blank=True, null=True)
    status = models.SmallIntegerField(u'Status', choices=STATUS, blank=True, null=True)


class Postagem(models.Model):
    titulo = models.CharField(u'Título', max_length=50, blank=False, null=False)
    texto = models.TextField(u'Texto', blank=False, null=False)
    data = models.DateField(u'Data', auto_now_add=True)
    autor = models.ForeignKey(User, blank=False, null=False)


class Evento(models.Model):
    titulo = models.CharField(u'Título', max_length=50, blank=False, null=False)
    descricao = models.TextField(u'Texto', blank=False, null=False)
    descricao = models.URLField(u'Local', blank=False, null=False)
    inicio = models.DateField(u'Início', blank=True, null=True)
    termino = models.DateField(u'Término', blank=True, null=True)
    autor = models.ForeignKey(User, blank=False, null=False)

    def __unicode__(self):
        return self.titulo
