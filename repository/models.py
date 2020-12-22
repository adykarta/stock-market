# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

# Create your models here.


class StockRepository:
    BUCKET = 'Stocks'

    def __init__(self, client):
        self.client = client

    def add(self, name, quantity, price):
        datas = {"name": name,
                 "quantity": quantity,
                 "price": price}
        datas = json.dumps(datas)
        if(self.client.bucket(self.BUCKET).get(name).data == None):

            riak_obj = self.client.bucket(self.BUCKET).new(name, data=datas)

            print("created")
            return riak_obj.store()
        else:
            print("Already created")
            return "Stock already added"

    def set(self, name, quantity):
        datas = {"name": name,
                 "quantity": quantity,
                 }
        riak_obj = self.client.bucket(self.BUCKET).get(name)
        data = json.loads(riak_obj.data)
        prevData = data["stocks"]
        prevData.append(datas)

        data["stocks"] = prevData
        updatedData = json.dumps(data)
        print(updatedData)
        riak_obj.data = updatedData
        return riak_obj.store()
        # print(riak_obj.data.stocks)
        # riak_obj.data.stocks = json.dumps(prevData)

        # riak_obj.data = data
        # return riak_obj.store()

    def get(self, name):
        riak_obj = self.client.bucket(self.BUCKET).get(name)
        return riak_obj.data


class UserRepository:
    BUCKET = 'Users'

    def __init__(self, client):
        self.client = client

    def add(self, username, password):
        datas = {"username": username,
                 "password": password,
                 "stocks": []
                 }
        datas = json.dumps(datas)
        if(self.client.bucket(self.BUCKET).get(username).data == None):

            riak_obj = self.client.bucket(
                self.BUCKET).new(username, data=datas)

            print("created")
            return riak_obj.store()
        else:
            print("Already created")
            return "User already added"

    def set(self, username, name, quantity):
        datas = {"name": name,
                 "quantity": quantity,
                 }
        riak_obj = self.client.bucket(self.BUCKET).get(username)
        data = json.loads(riak_obj.data)
        prevData = data["stocks"]
        prevData.append(datas)

        data["stocks"] = prevData
        updatedData = json.dumps(data)
        print(updatedData)
        riak_obj.data = updatedData
        return riak_obj.store()
        # print(riak_obj.data.stocks)
        # riak_obj.data.stocks = json.dumps(prevData)

        # riak_obj.data = data
        # return riak_obj.store()

    def get(self, username):
        riak_obj = self.client.bucket(self.BUCKET).get(username)
        return riak_obj.data


class SessionRepository:
    BUCKET = 'Sessions'

    def __init__(self, client):
        self.client = client

    def add(self, username, session_id, last_login):
        datas = {"username": username,
                 "session_id": session_id,
                 "last_login": last_login,
                 }
        datas = json.dumps(datas)
        if(self.client.bucket(self.BUCKET).get(username).data == None):

            riak_obj = self.client.bucket(
                self.BUCKET).new(username, data=datas)

            print("created")
            return riak_obj.store()
        else:
            print("Already login")
            return "Already login"

    def get(self, username):
        riak_obj = self.client.bucket(self.BUCKET).get(username)
        return riak_obj.data

    def delete(self, username):
        riak_obj = self.client.bucket(self.BUCKET).get(username)
        riak_obj.delete()
        return


class TransactionRepository:
    BUCKET = 'Transactions'

    def __init__(self, client):
        self.client = client

    def add(self, username, stock_name, quantity, time):
        datas = {"username": username,
                 "stock_name": stock_name,
                 "quantity": quantity,
                 "time": time
                 }
        datas = json.dumps(datas)
        riak_obj = self.client.bucket(
            self.BUCKET).new(username, data=datas)
        print("created")
        return riak_obj.store()

    def get(self, username):
        riak_obj = self.client.bucket(self.BUCKET).get(username)
        return riak_obj.data
