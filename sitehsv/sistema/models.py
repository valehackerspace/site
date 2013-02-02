# coding: utf-8
from django.db import models


class Projetos(models.Model):
    nome = models.CharField(u'Projeto', max_length=50, blank=False, null=False)
    descricao = models.TextField(u'Descrição', blank=False, null=False)
    inicio = models.DateField(label=u'Data de Início', auto_now_add=True)
    previsao_termino = models.DateField(label=u'Previsão de Término')
