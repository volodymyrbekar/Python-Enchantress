from dataclasses import dataclass
from flask_restful import Api, Resource
from flask import Flask, request
from datetime import datetime

amazon_killer = Flask(__name__)
api = Api(amazon_killer)

USERS_DATABASE = {}
CART_DATABASE = {}
user_counter = 1
cart_counter = 1


@dataclass()
class NoSuchUser(Exception):
    user_id: int


@dataclass()
class NoSuchCart(Exception):
    cart_id: int


@amazon_killer.route(NoSuchUser)
def no_such_user_handler(self, error):
    return {"error": "no such user with id 1"}, 404


@amazon_killer.route(NoSuchCart)
def no_such_cart_handle(error):
    return {"error": "no such cart with id 1"}, 404


class Users(Resource):
    @staticmethod
    def post():
        global user_counter
        user = request.json
        user["user_id"] = user_counter
        response = {
            "registration_timestamp": datetime.now().isoformat(),
            "user_id": user_counter
        }
        user["registration_timestamp"] = response["registration_timestamp"]
        USERS_DATABASE[user_counter] = user
        user_counter += 1
        return response, 201

    @staticmethod
    def get(user_id):
        try:
            user = USERS_DATABASE[user_id]
        except KeyError:
            raise NoSuchUser(user_id)
        else:
            return user

    @staticmethod
    def put(user_id):
        user = request.json
        response = {"status": "success"}
        try:
            USERS_DATABASE[user_id]["name"] = user["name"]
            USERS_DATABASE[user_id]["email"] = user["email"]
        except KeyError:
            raise NoSuchUser(user_id)
        else:
            return response, 200

    @staticmethod
    def delete(user_id):
        global user_counter
        response = {"status": "success"}
        try:
            USERS_DATABASE[user_id].pop()
            user_counter -= 1
        except KeyError:
            raise NoSuchUser(user_id)
        else:
            return response, 200


class Carts(Resource):
    @staticmethod
    def post():
        global cart_counter
        cart = request.json
        response = {
            "cart_id": cart_counter,
            "creating_time": datetime.now().isoformat()
        }
        cart["creating_time"] = response["creating_time"]
        cart["cart_id"] = cart_counter
        CART_DATABASE[cart_counter] = cart
        cart_counter += 1

        return response, 201

    @staticmethod
    def get(cart_it):
        try:
            cart = CART_DATABASE[cart_it]
        except KeyError:
            raise NoSuchCart
        else:
            return cart

    @staticmethod
    def put(cart_id):
        cart = request.json
        response = {"status": "success"}
        try:
            CART_DATABASE[cart_id]["products"] = cart["products"]
            CART_DATABASE[cart_id]["registration_time"] = cart["registration_time"]
        except KeyError:
            raise NoSuchCart
        else:
            return response, 200

    @staticmethod
    def delete(cart_id):
        global cart_counter
        response = {'status': 'success'}
        try:
            CART_DATABASE[cart_id].pop()
        except KeyError:
            raise NoSuchCart(cart_id)
        else:
            return response, 200


api.add_resource(Users, "/<int: user_id>", "/users")
api.add_resource(Carts, "/<int: cart_id>", "/carts")

if __name__ == "__main__":
    amazon_killer.run(debug=True)
