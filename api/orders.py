# python packages
from flask_restful import Resource, request
from flask_jwt import jwt_required
from flask_jwt_extended import jwt_required
from flask import jsonify
# local packages
from models.orders import OrdersModel

class Orders(Resource):
 
    @jwt_required()  # Requires dat token
    def get(self, order_id):
        order = OrdersModel.find_by_order_id(order_id)
        if order:
            return jsonify({'orders' : order.json()})
        return {'message': 'Order not found'}, 404

    @jwt_required()
    def post(self):
        data = request.get_json(force=True)
        data['_id'] = 0
        order = OrdersModel(data)

        try:
            order.insert_to_db()
        except:
            return {"message": "An error occurred inserting the order."}, 500
        
        return order.json(), 201

    @jwt_required()
    def delete(self, order_id):
        order = OrdersModel.find_by_order_id(order_id)
        if order:
            order.delete_from_db()

            return {'message': 'order has been deleted'}

    @jwt_required()
    def put(self, order_id):
        # Create or Update
        data = request.get_json(force=True)
        order = OrdersModel.find_by_order_id(order_id)

        if order is None:
            order = OrdersModel(data['action'],data['symbol'], data['price'], data['order_type'],
                            data['order_size'], data['value'], data['account_id'])
        else:
            order.price = data['price']
            order.order_size = data['order_size']
            order.value = data['value']
            order.order_type = data['order_type']

        order.update_to_db()

        return order.json()


class OrdersList(Resource):
    @jwt_required()
    def get(self, account_id):
        return {'orders': OrdersModel.find_all_orders_by_account(account_id)} 
