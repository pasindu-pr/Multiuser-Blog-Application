from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import find_dotenv, load_dotenv 
from flask_login import LoginManager
import os

db = SQLAlchemy()
load_dotenv(find_dotenv())

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("FLASK_APP_SECRET") 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/blogdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)

    from .views.blogviews import blogviews
    from .views.authviews import authviews
    from .views.adminViews import adminviews

    from .models import Post, User, Comment

    # with app.app_context():
    #     db.create_all() 

    app.register_blueprint(blogviews, url_prefix="/")
    app.register_blueprint(authviews, url_prefix="/auth") 
    app.register_blueprint(adminviews, url_prefix="/admin")

    login_manager = LoginManager()
    login_manager.login_view = 'authviews.login'
    login_manager.login_message = 'Please login to your account in order to continue!'
    login_manager.login_message_category = 'error'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app