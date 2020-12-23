# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from repository.db import myClient
from django.contrib import messages
from repository.models import SessionRepository, UserRepository
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

@csrf_exempt
def getUser(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        userRepo = UserRepository(myClient)
        data = json.loads(userRepo.get(username))
        uname = data.get("username")
        stocks = data.get("stocks")
        time = data.get("buy_time")
        return JsonResponse({"message": "success", 'uname': uname, 'daftar_saham': stocks, "buy_time": time}, safe=False)
    else:
        return JsonResponse({"message": "failed"},  safe=False)


def profil(request):
    return render(request, 'profil.html', content_type='html')
