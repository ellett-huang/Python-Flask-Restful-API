from flask_restful import Resource, request
from flask_jwt import JWT
from flask_jwt_extended import jwt_required

from models.users import UsersModel

class Users(Resource):    
    @jwt_required()
    def get(self):        
        data = request.get_json(force=True)
        user = UsersModel.find_by_username(data['username'])
        if user:
            return {'user': user}
    
    @jwt_required()
    def delete(self):
        data = request.get_json(force=True)
        user = UsersModel.find_by_username(data['username'])
        if user:
            user.delete_from_db()
            return {'message': 'user {} has been deleted'.format(data['username'])}

class UserRegister(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json(force=True)
        if UsersModel.find_by_username(data['username']):
            return {'message': 'Username is existed, please use another name.'}, 400
        data['_id'] = 0
        user = UsersModel(data)
        user.insert_to_db()

        return {'message': 'user has been created successfully.'}, 201
