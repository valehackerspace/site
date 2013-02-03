# coding: utf-8
from django.http import Http404, HttpResponse


def home(request):
    return HttpResponse('Home')


def eventos_list(request):
    return HttpResponse('Eventos')


def projetos_list(request):
    return HttpResponse('Projetos')


def post(request, pk=None):
    return HttpResponse('Post')


def evento(request, pk=None):
    return HttpResponse('Evento')


def projeto(request, pk=None):
    return HttpResponse('Projeto')
