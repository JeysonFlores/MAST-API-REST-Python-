from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/mastdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TURN_ON_TIME'] = datetime.datetime.utcnow()


db = SQLAlchemy(app)
ma = Marshmallow(app)

from db import *
from schemes import *

user_schema = UsersSchema()
emp_schema = EmployeesSchema()
emps_schema = EmployeesSchema(many=True)
client_schema = ClientsSchema()
clients_schema = ClientsSchema(many=True)
prod_schema = ProductsSchema()
prods_schema = ProductsSchema(many=True)

from routes import *


if __name__ == "__main__":
    app.run(debug=True)