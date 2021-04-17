# flask packages
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask_jwt_extended import jwt_required
# local packages
from models.accounts import AccountsModel

class Accounts(Resource):
    @jwt_required()  # Requires dat token
    def get(self, username, account_id):
        account = AccountsModel.find_by_id(username, account_id)
        if account:
            return account.json()
        return {'message': 'account not found'}, 404

    @jwt_required()  # Requires dat token
    def put(self, username,account_id):
        data = request.get_json(force=True)
        account = AccountsModel.find_by_id(username, account_id)
        if account:  
            try:
                account.account_name = data['account_name']
                account.update_to_db()
            except:
                return {"message": "An error occurred updating the account."}, 500

        return account.json(), 201

    @jwt_required()  # Requires dat token
    def post(self, username):
        data = request.get_json(force=True)
        data['username'] = username
        data['_id'] = 0
        if AccountsModel.find_by_name(username, data['account_name']):
            return {'message': "An account '{}' already exists.".format(account_name)}, 400

        account = AccountsModel(data)
        try:
            account.insert_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return account.json(), 201

    @jwt_required()  # Requires dat token
    def delete(self, username, account_id):
        account = AccountsModel.find_by_id(username, account_id)
        if account:
            account.delete_from_db()

        return {'message': 'Acount deleted'}


class AccountsList(Resource):
    @jwt_required()  # Requires dat token
    def get(self, username):
        return {'accounts': list(map(lambda x: x, AccountsModel.all(username) ))} #Lambda way
