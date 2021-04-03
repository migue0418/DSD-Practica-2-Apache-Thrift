# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import os
from thrift_code import cliente

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    if request.method == 'POST':
        info = {
            'expresion': request.POST['expresion'],
            'resultado': 0.0,
            'error': ''
        }
        cliente.main(info)
    else:
        info = {
            'expresion': '',
            'resultado': '',
            'error': ''
        }
    return render(request, os.path.join(BASE_DIR, 'templates/calculadora/index.html'), info)
