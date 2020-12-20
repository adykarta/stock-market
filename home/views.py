# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    return render(request, 'home.html', {
        'foo': 'bar',
    }, content_type='html')
    