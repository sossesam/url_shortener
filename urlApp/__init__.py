#!/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/sanmi/Desktop/url_shortener/urlApp/test.db"
    

    from urlApp.users.routes import users


    app.register_blueprint(users)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


    
