# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from repository.db import myClient
from django.contrib import messages
from repository.models import SessionRepository, UserRepository
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def login(request):
    if(request.method == "POST"):

        username = request.POST.get('username')
        password = request.POST.get('password')

        sessionRepo = SessionRepository(myClient)
        userRepo = UserRepository(myClient)
        if(username == "" or password == ""):
            messages.success(request, "Periksa kembali")
            return JsonResponse({"message": "Periksa kembali"}, safe=False)

        if(sessionRepo.get(username) == None):
            if(userRepo.get(username) != None):
                data = json.loads(userRepo.get(username))
                dateTimeObj = datetime.now()
                timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
                if(data.get("password") == password):
                    sessionRepo.add(username, "session", timestampStr
                                    )
                    messages.success(request, username)
                    return JsonResponse({"username": username, "message": "success"}, safe=False)
                else:
                    messages.error(request, "password salah")
                    return JsonResponse({"message": "Password salah"}, safe=False)

            else:
                messages.error(request, "username tidak terdaftar")
                return JsonResponse({"message": "Username tidak terdaftar"}, safe=False)

        else:
            messages.error(request, "already logged")
            return JsonResponse({"message": "Already logged"}, safe=False)

    else:
        messages.error(request, "gagal")
        return HttpResponseRedirect('/registration/login')


@csrf_exempt
def signup(request):
    if(request.method == "POST"):

        username = request.POST.get('username')
        password = request.POST.get('password')
        userRepo = UserRepository(myClient)
        if(username == "" or password == ""):
            messages.success(request, "Periksa kembali")
            return HttpResponseRedirect('/registration/signup')
        if(userRepo.get(username) == None):
            userRepo.add(username, password)
            messages.success(request, "success")
            return HttpResponseRedirect('/registration/login')
        else:
            messages.error(request, "Username already taken")
            return HttpResponseRedirect('/registration/signup')
    else:
        messages.error(request, "gagal")
        return HttpResponseRedirect('/registration/signup')


@csrf_exempt
def logout(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        sessionRepo = SessionRepository(myClient)
        if(sessionRepo.get(username) != None):
            sessionRepo.delete(username)
            return JsonResponse({"message": "success"}, safe=False)
        else:
            return JsonResponse({"message": "Username have not logged in"}, safe=False)


def loginPage(request):
    return render(request, 'login.html', {
        'foo': 'bar',
    }, content_type='html')


def signupPage(request):
    return render(request, 'signup.html', {
        'foo': 'bar',
    }, content_type='html')
