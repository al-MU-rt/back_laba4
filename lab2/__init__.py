from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "abcd"
app.config['JWT_ALGORITHM'] = "HS256"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://avnadmin:AVNS_zJ_kWB7bm85wFn1mbSQ@pg-c451c97-anton25348-e158.a.aivencloud.com:17075/defaultdb?sslmode=require"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

import lab2.views
import lab2.models
