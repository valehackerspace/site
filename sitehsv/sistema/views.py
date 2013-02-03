# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from sistema.models import (Evento, Postagem, Projeto)


def home(request):
    return HttpResponse('Home')


def eventos_list(request):
    eventos = Evento.objects.all().order_by('inicio')

    paginator = Paginator(eventos, 10)
    page = request.GET.get('page')
    try:
        evento_list = paginator.page(page)
    except PageNotAnInteger:
        evento_list = paginator.page(1)
    except EmptyPage:
        evento_list = paginator.page(paginator.num_pages)

    return render(request, "sistema/evento/eventos.html", {'evento_list': evento_list,
        'is_paginated': paginator.num_pages > 1, 'page_obj': evento_list,
        'paginator': paginator})

    return HttpResponse('Eventos')


def projetos_list(request):
    return HttpResponse('Projetos')


def post(request, pk=None):
    post = get_object_or_404(Postagem, pk=pk)
    return HttpResponse('Post')


def evento(request, pk=None):
    evento = get_object_or_404(Evento, pk=pk)
    return HttpResponse('Evento')


def projeto(request, pk=None):
    projeto = get_object_or_404(Projeto, pk=pk)
    return HttpResponse('Projeto')
