# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import os

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    return render(request, os.path.join(BASE_DIR, 'templates/calculadora/index.html'), {})
