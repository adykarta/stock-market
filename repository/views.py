# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import pandas as pd

import json
from models import StockRepository, UserRepository

import os
from django.conf import settings

from db import myClient


def process_data():
    dataset = open(os.path.join(settings.BASE_DIR,
                                './repository/data/nse.csv'))
    new_data = pd.read_csv(dataset)

    processed_data = new_data.drop(
        columns=["SERIES", "HIGH", "LOW", "CLOSE", "LAST", "PREVCLOSE", "TOTTRDVAL", "TIMESTAMP", "TOTALTRADES", "ISIN"])
    processed_data = processed_data.dropna()
    processed_data = processed_data.head(1000)
    # print(processed_data)
    return seed(processed_data)


def seed(data):

    # stocks = myClient.bucket('stocks')
    # users = myClient.bucket('users')
    stockRepo = StockRepository(myClient)
    userRepo = UserRepository(myClient)
    # print(stockRepo)
    for i, row in data.iterrows():
        name = row['SYMBOL']
        price = row['OPEN']
        quantity = row['TOTTRDQTY']
        stockRepo.add(name, quantity, price)

    stock_data = []
    for i, row in data.iterrows():
        name = row['SYMBOL']
        stock_data.append(json.loads(stockRepo.get(name)))
    # print(stockRepo.get(name))

    user_data = []
    # Init user
    username_admin = "admin"
    password_admin = "admin"
    userRepo.add(username_admin, password_admin)
    usr = json.loads(userRepo.get(username_admin))
    user_data.append(usr)

    # print(stock_data)
    datas = {}
    datas['stocks'] = stock_data
    datas['users'] = user_data

    return json.dumps(datas)


def index(request):
    if request.method == 'GET':
        datas = process_data()

        return HttpResponse(process_data())
