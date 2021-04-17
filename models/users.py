# python packages
import json
from bson import ObjectId
from flask_jwt_extended import jwt_required
# local packages
from core.db import mongodb

class UsersModel():
    users = mongodb['users']

    def __init__(self, user):
        self.id = str(user['_id'] )
        self.username = user['username']
        self.password = user['password']
        self.bio = user['bio']
        self.image = user['image']
        self.email = user['email']    

    @classmethod
    def find_by_username(cls, username):
        user = cls.users.find_one({'username' : username}) 
        if user:
            return UsersModel(user)
        else:
            return None

    @classmethod
    def find_by_userID(cls, id):
        user = cls.users.find_one({'_id' : ObjectId(id)}) 
        if user:
            return UsersModel(user)
        else:
            return None

    def json(self):
        return {'id': str(self.id),'username': self.username,
                'password': self.password,'bio': self.bio,
                'email': self.email,'image': self.image}

    @jwt_required()  # Requires dat token
    def insert_to_db(self):  # inserting data
        self.users.insert({ 'username': self.username,
                            'password': self.password,
                            'bio': self.bio,
                            'image': self.image,
                            'email': self.email})

    @jwt_required()  # Requires dat token
    def update_to_db(self):
        myquery = { "_id": ObjectId(self.id) }
        newvalues = { "$set": { 'password': self.password } }

        self.users.update_one(myquery, newvalues)

    @jwt_required()  # Requires dat token
    def delete_from_db(self):
        self.users.delete_one({ "_id": ObjectId(self.id) })
