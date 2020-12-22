from django.shortcuts import render
from repository.models import StockRepository, TransactionRepository, UserRepository, StockRepository
from repository.db import myClient
import requests, json
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import datetime
from json import dumps

# Create your views here.

def detail(request, *args, **kwargs):
    nama = request.GET.get('nama', '')
    stockRepo = StockRepository(myClient)
    data = json.loads(stockRepo.get(nama))
    response = {
        "stock" : data
    }
    return render(request, 'detail.html', response, content_type='html')
    
@csrf_exempt
def beliSaham(request):
    if(request.method == "POST"):
        namaSaham = request.POST.get('namaSaham')
        hargaSaham = request.POST.get('hargaSaham')
        jumlahSaham = request.POST.get('jumlahSaham')
        jumlahBeli = request.POST.get('jumlahBeli')
        username = request.POST.get('usernama')
        waktu = datetime.datetime.now()
        waktuString = str(waktu)

        # waktuEdit = waktu.strftime('%Y-%m-%dT%H:%M:%S.%f')
        # waktuJson = json.dumps(waktuEdit)
        # print(waktuJson)
        transRepo = TransactionRepository(myClient)
        transRepo.add(username, namaSaham, str(jumlahBeli), waktuString)

        stockRepo = StockRepository(myClient)
        intJumlahSaham = int(jumlahSaham)
        intBeliSaham = int(jumlahBeli)
        tempJumlahSaham = intJumlahSaham - intBeliSaham
        stockRepo.set(namaSaham, tempJumlahSaham)
        
        userRepo = UserRepository(myClient)
        userRepo.set(username, namaSaham, str(jumlahBeli))

        return HttpResponseRedirect('/')
    else:
        messages.error(request, "gagal")
        return HttpResponseRedirect('/detailStock/beliSaham')