# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from repository.models import StockRepository
from django.http import JsonResponse
from repository.db import myClient
import requests, json

# Create your views here.


def home(request):
    response = {
        "stocks": get_all_data()
    }
    # print(response)
    return render(request, 'home.html', response, content_type='html')

def get_all_data():
    stockRepo = StockRepository(myClient)
    response = requests.get('http://coordinator:8098/buckets/Stocks/keys?keys=true')
    keys = response.json()[u'keys']
    allStocks = []

    for x in keys:
        stock_obj = json.loads(stockRepo.get(x))
        allStocks.append(stock_obj)
        
    return allStocks
    