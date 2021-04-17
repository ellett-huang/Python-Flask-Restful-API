# flask packages
from bson.json_util import json, dumps
from bson import ObjectId
# local packages
from core.db import mongodb

class OrdersModel():    
    orders = mongodb['orders']

    def __init__(self, order):
        self.id = order['_id']
        self.action = order['action']
        self.symbol = order['symbol']
        self.price = order['price']
        self.order_type = order['order_type']
        self.order_size = order['order_size']
        self.value = order['value']
        self.account_id = order['account_id']

    def json(self):
        return {'action': self.action, 'symbol': self.symbol, 'price': self.price, 'value': self.value, 'order_type': self.order_type, 'order_size': self.order_size,'account_id': str(self.account_id)}

    @classmethod
    def find_by_order_id(cls, id):
        order = cls.orders.find_one({'_id' : ObjectId(id)}) 
        if order:
            return OrdersModel(order)
        else:
            return None

    @classmethod
    def find_all_orders_by_account(cls, account_id):
        orders = cls.orders.find({'account_id' : ObjectId(account_id)}) 
        return json.loads(dumps(orders)) if orders else None 

    @classmethod
    def find_all_orders_by_user(cls, username):
        orders = cls.orders.find({'username' : username}) 
        return json.loads(dumps(orders)) if orders else None      

    def insert_to_db(self):  # inserting data
        self.orders.insert({'action': self.action,
                            'symbol': self.symbol,
                            'price': self.price,
                            'order_type': self.order_type,
                            'order_size': self.order_size,
                            'value': self.value,
                            'account_id': ObjectId(self.account_id)})

    def update_to_db(self):
        myquery = { "_id": self.id }
        newvalues = { "$set": { "action": self.action,
                                "price": self.price,
                                "order_type": self.order_type,
                                "order_size": self.order_size } }

        self.orders.update_one(myquery, newvalues)

    def delete_from_db(self):
        self.orders.delete_one({ "_id": ObjectId(self.id) })
