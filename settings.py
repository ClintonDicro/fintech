from flask import Flask,jsonify,request,make_response
from werkzeug.security import check_password_hash,generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.sql import func
from sqlalchemy_utils import ChoiceType
from flask_migrate import Migrate
from datetime import datetime,date
import random




app = Flask(__name__)
app.config["SECRET_KEY"] = "dicro"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345@localhost/fintech"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


CORS(app)


db = SQLAlchemy(app)

migrate=Migrate(app,db)




def Random_number():
    number=random.randint(0000,9999)
    return number