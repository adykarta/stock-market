# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class StockRepository:
    BUCKET = 'Stocks'

    def __init__(self, client):
        self.client = client

    def add(self, name, quantity, price):
        datas = {"name": name,
                 "quantity": quantity,
                 "price": price}

        if(self.client.bucket(self.BUCKET).get(name).data == None):

            riak_obj = self.client.bucket(self.BUCKET).new(name, data=datas)

            print("created")
            return riak_obj.store()
        else:
            print("Already created")
            return "Stock already added"

    def get(self, name):
        riak_obj = self.client.bucket(self.BUCKET).get(name)
        return riak_obj.data
