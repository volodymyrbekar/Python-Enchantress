from flask import request
from flask_login import login_user, login_required, logout_user
from flask_restful import Resource
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class Login(Resource):
    @staticmethod
    def get(self):
        return {"login page status": 'success'}, 200

    @staticmethod
    def post(self):
        response = request.get_json()
        email = response["email"]
        password = response["password"]
        saved_data = True if bool(response["saved_data"]) else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return {"error": "User does not exist or password in not correct"}, 404

        login_user(user, saved_data=saved_data)
        login_user(user)
        return {"status": "success"}, 200


class SignUp(Resource):
    @staticmethod
    def get(self):
        return {"message": {"enter your data: email, name, password"}}, 200

    @staticmethod
    def post(self):
        data = request.get_json()
        email = data['email']
        name = data['name']
        password = data['password']

        user = User.query.filter_by(email=email).first()

        if user:
            return {'error': "email already exist"}, 404

        new_user = User(email=email, name=name, password=generate_password_hash(password, method="sha256"))

        db.session.add(new_user)
        db.session.commit()

        return {"status": {"success"}}, 200


class LogOut(Resource):
    @staticmethod
    @login_required
    def get(self):
        logout_user()
        return {"status": "success"}, 200
