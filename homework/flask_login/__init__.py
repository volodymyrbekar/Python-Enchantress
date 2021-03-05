from flask.cli import AppGroup
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_restful import Api
import click

db = SQLAlchemy()
user_cli = AppGroup('user')
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config['SECRET_KEY'] = 'my_secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True

    login_manager.init_app(app)
    db.init_app(app)

    from .auth import Login, SignUp, LogOut

    api.add_resource(Login, "/login")
    api.add_resource(Login, "/signup")
    api.add_resource(Login, "/logout")

    from .main import MainPage, Profile, OrderPage
    api.add_resource(MainPage, "/")
    api.add_resource(Profile, "/profile")
    api.add_resource(OrderPage, '/order')

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.cli.command("create-db")
    def create_db():
        db.create_all()

    app.cli.add_command(user_cli)

    return app

