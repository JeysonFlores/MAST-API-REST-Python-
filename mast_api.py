from flask import Flask, Request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/mast'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50))
    address = db.Column(db.String(60))
    email = db.Column(db.String(50))
    telephone = db.Column(db.Integer())   
    job = db.Column(db.String(15))
    gender = db.Column(db.String(10))
    status = db.Column(db.String(1))

    def __init__(self,name,address,email,telephone,job,gender):
        self.name = name
        self.address = address
        self.email = email
        self.telephone = telephone
        self.job = job
        self.gender = gender
        status = 'A'


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(80))
    contact = db.Column(db.String(40))
    telephone = db.Column(db.Integer())
    status = db.Column(db.String(1))

    def __init__(self, name, address, contact, telephone):
        self.name = name
        self.address = address
        self.contact = contact
        self.telephone = telephone
        self.status = 'A'


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    quantity = db.Column(db.Integer())
    price = db.Column(db.Float)
    description = db.Column(db.String(120))
    status = db.Column(db.String(1))

    def __init__(self, name, quantity, price, description):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.description = description
        self.status = 'A'


db.create_all()


class EmployeesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'email', 'telephone', 'job', 'gender', 'status')


class ClientsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'contact', 'telephone', 'status')


class ProductsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'quantity', 'price', 'description', 'status')

emp_schema = EmployeesSchema()
client_schema = ClientsSchema()
prod_schema = ProductsSchema()

@app.route('/test')
def testroute():
    return "Received"


if __name__ == "__main__":
    app.run(debug=True)

# --------------------- Jeyson Antonio Flores Deras --- August 2020 ------------------------------