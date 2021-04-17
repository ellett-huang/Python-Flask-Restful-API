# flask packages
from flask import Flask, app
from flask_jwt import JWT
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# local packages
from api.routes import create_routes

def get_flask_app() -> app.Flask:
    app = Flask(__name__)
    app.secret_key = 'talett.corp.python'

    # init api and routes
    api = Api(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    create_routes(api) 
    # init jwt manager
    jwt = JWTManager(app=app)
    return app 

if __name__ == '__main__':
    app = get_flask_app()
    # When you need to debug your code in your local, set debug=True
    app.run(debug=True)  

