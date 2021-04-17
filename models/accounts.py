# flask packages
from bson.json_util import json, dumps
from bson import ObjectId
# local packages
from core.db import mongodb
from models.orders import OrdersModel

class AccountsModel():
    accounts = mongodb['accounts']

    def __init__(self, account):
        self.account_id = account['_id']
        self.account_name = account['account_name']
        self.username = account['username']

    def json(self):
        return json.loads(dumps({'account_id': self.account_id,
                                 'account_name': self.account_name}))

    @classmethod
    def find_by_id(cls, username, account_id):
        account = cls.accounts.find_one({'_id' : ObjectId(account_id),
                                         'username' : username}) 
        if account:
            return AccountsModel(json.loads(dumps(account)))
        else:
            return None

    @classmethod
    def find_by_name(cls, username, account_name):
        account = cls.accounts.find_one({'account_name' : account_name,
                                         'username' : username}) 
        if account:
            return AccountsModel(json.loads(dumps(account)))
        else:
            return None

    @classmethod
    def all(cls, username):
        accounts = cls.accounts.find({'username' : username}) 
        return json.loads(dumps(accounts)) if accounts else None

    def insert_to_db(self):  # inserting data
        self.accounts.insert({'account_name': self.account_name,
                              'username': self.username})

    def update_to_db(self):
        myquery = { "_id": ObjectId(self.account_id['$oid']) }
        newvalues = { "$set": {'account_name': self.account_name } }

        self.accounts.update_one(myquery, newvalues)

    def delete_from_db(self):
        self.accounts.delete_one({ "_id": ObjectId(self.account_id['$oid']) })
