# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.user import UsersApi, UserApi
from api.products import ProductsApi, ProductApi


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    api.add_resource(SignUpApi, "/authentication/signup/")
    api.add_resource(LoginApi, "/authentication/login/")

    api.add_resource(UsersApi, "/user/")
    api.add_resource(UserApi, "/user/<user_id>")

    api.add_resource(ProductsApi, "/products/")
    api.add_resource(ProductApi, "/product/<product_id>")

