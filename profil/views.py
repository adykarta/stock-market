# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from repository.db import myClient
from django.contrib import messages
from repository.models import SessionRepository, UserRepository
# from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def profil(request):
    username = request.GET.get('username')

    userRepo = UserRepository(myClient)
    data = json.loads(userRepo.get(username))

    uname = data.get("username")
    stocks = data.get("stocks")

    return render(request, 'profil.html', {
        'uname': uname, 'daftar_saham': stocks
    }, content_type='html')


