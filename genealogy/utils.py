#-*- coding: utf-8 -*-

#python
import re
import json

#django
from django import shortcuts
from django.template import RequestContext, loader
from django.contrib import messages
from django.contrib.messages.api import get_messages
from django.core.paginator import EmptyPage, InvalidPage
from django.http import HttpResponse

def render_to_response(request, *_arg):
    """
    Nasze generowanie szablonu, bierze pod uwage kontekst z userem
    """
    arg = __populate_response_args(request, *_arg)
    return shortcuts.render_to_response(*arg)

def __populate_response_args(request, *_arg):
    """
    Dodaje argumenty związane z kontekstem, zawierającym informacje o zalogowanym
    użytkowniku, komunikatami z django.contrib.messages oraz oryginalnym requestem.
    """
    arg = []
    for x in _arg:
        arg.append(x)
    arg.append(RequestContext(request))
    arg[1]['messages'] = get_messages(request)
    arg[1]['request'] = request
    return arg
