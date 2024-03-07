from flask import Flask
from flask_sqlalchemy import SQLAlchemy, session
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Blender_12@localhost/flask_aws'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from .views import views
    # from .auth import auth

    # initialise SQLAlchemy with flask 
    db.init_app(app)

    app.register_blueprint(views, url_prefix="/")
    # app.register_blueprint(auth, url_prefix="/")

    from .models import Image

    return app

