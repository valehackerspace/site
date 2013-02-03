# coding: utf-8
from django.db import models

STATUS = (
    (1, u'Proposta'),
    (2, u'Em Andamento'),
    (2, u'Concluído'),
    (2, u'Abandonado'),
    )


class Projetos(models.Model):
    nome = models.CharField(u'Projeto', max_length=50, blank=False, null=False)
    descricao = models.TextField(u'Descrição', blank=False, null=False)
    inicio = models.DateField(label=u'Data de Início', blank=True, null=True)
    previsao_termino = models.DateField(label=u'Previsão de Término', blank=True, null=True)
    status = models.SmallIntegerField(u'Status', choices=STATUS, blank=True, null=True)
