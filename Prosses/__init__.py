from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from Prosses import config
from sqlalchemy import create_engine
from flask_login import LoginManager
from datetime import *
# from Prosses.models import Admin, Product, User

app = Flask(__name__)
app.secret_key = "hahahahahaha"
app.permanent_session_lifetime = timedelta(hours=3)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:""@localhost/myapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

engine = create_engine("mysql+pymysql://root@localhost/myapp")
dbs = scoped_session(sessionmaker(bind=engine))

login_manager = LoginManager()
login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
# 	return User.query.get(int(user_id))

# @login_manager.user_loader
# def load_user(user_id):
# 	return Admin.query.get(int(user_id))


db = SQLAlchemy(app)