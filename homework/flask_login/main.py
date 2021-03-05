from flask_login import login_required, current_user
from flask import request, jsonify
from flask_restful import Resource
from .models import Order

from . import db


class MainPage(Resource):
    @staticmethod
    def get(self):
        return {"status": "success"}, 200


class Profile(Resource):
    @staticmethod
    @login_required
    def get(self):
        return {"name": current_user.name}, 200


class OrderPage(Resource):
    @staticmethod
    @login_required
    def get(self):
        user = current_user.id
        orders = Order.query.filter_by(user_id=current_user.user_id).all()

        return jsonify({
            'status': "success",
            "user_id": current_user.user_id,
            'orders': orders
        }), 200
