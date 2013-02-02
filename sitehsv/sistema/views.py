# coding: utf-8
from django.http import Http404, HttpResponse


def home(request):
    return HttpResponse('A')
