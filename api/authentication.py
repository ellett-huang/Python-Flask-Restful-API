# python packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
# python packages
from werkzeug.security import safe_str_cmp
from datetime import timedelta

# local packages
from models.users import UsersModel
from api.errors import unauthorized

class Auth(Resource): 
    def post(self) -> Response: 
        data = request.get_json(force=True)
        user = UsersModel.find_by_username(data['user']['username'])
        auth_success = user and safe_str_cmp(user.password, data['user']['password'])
        if not auth_success:
            return unauthorized()
        else:
            expiry = timedelta(days=5)
            access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
            
            return jsonify({'user': {'token': access_token,
                                     'bio': user.bio,
                                     'email': user.email,
                                     'image': f"{user.image}",  
                                     'username': f"{user.username}"}})