from api.orders import Orders, OrdersList
from api.accounts import Accounts, AccountsList
from api.users import UserRegister, Users
from api.authentication import Auth

def create_routes(api):
    api.add_resource(Orders, '/orders/<string:order_id>', '/orders')
    api.add_resource(OrdersList, '/orderslist/<string:account_id>')
    api.add_resource(Users, '/users')
    api.add_resource(UserRegister, '/register')
    api.add_resource(Auth, '/auth')
    api.add_resource(Accounts, '/accounts/<string:username>/<string:account_id>','/accounts/<string:username>')
    api.add_resource(AccountsList, '/accountsList/<string:username>')