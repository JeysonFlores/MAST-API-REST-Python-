from flask import Flask, request, jsonify
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
    status = db.Column(db.String(2))

    def __init__(self,name,address,email,telephone,job,gender):
        self.name = name
        self.address = address
        self.email = email
        self.telephone = telephone
        self.job = job
        self.gender = gender
        self.status = 'A'


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
emps_schema = EmployeesSchema(many=True)
client_schema = ClientsSchema()
clients_schema = ClientsSchema(many=True)
prod_schema = ProductsSchema()
prods_schema = ProductsSchema(many=True)

@app.route('/test')
def testroute():
    return "Received"

@app.route('/employees', methods=['GET'])
def get_employees():
    all_employees = Employees.query.all()
    result = emps_schema.dump(all_employees)
    return jsonify(result)

@app.route('/employees/<id>', methods=['GET'])
def get_employee(id):
    emp = Employees.query.get(id)
    return emp_schema.jsonify(emp)

@app.route('/employees', methods=['POST'])
def add_employee():
    name = request.json['name']
    address = request.json['address']
    email = request.json['email']
    telephone = request.json['telephone']
    job = request.json['job']
    gender = request.json['gender']
    new_e = Employees(name,address,email,telephone,job,gender)
    db.session.add(new_e)
    db.session.commit()
    return emp_schema.jsonify(new_e)

@app.route('/employees/<id>', methods=['PUT'])
def mod_employee(id):
    emp = Employees.query.get(id)
    emp.name = request.json['name']
    emp.address = request.json['address']
    emp.email = request.json['email']
    emp.telephone = request.json['telephone']
    emp.job = request.json['job']
    emp.gender = request.json['gender']
    db.session.commit()
    return emp_schema.jsonify(emp)

@app.route('/clients', methods=['GET'])
def get_clients():
    all_clients = Clients.query.all()
    result = clients_schema.dump(all_clients)
    return jsonify(result)

@app.route('/clients/<id>', methods=['GET'])
def get_client(id):
    client = Clients.query.get(id)
    return client_schema.jsonify(client)

@app.route('/clients', methods=['POST'])
def add_client():
    name = request.json['name']
    address = request.json['address']
    contact = request.json['contact']
    telephone = request.json['telephone']
    new_c = Clients(name,address,contact,telephone)
    db.session.add(new_c)
    db.session.commit()
    return client_schema.jsonify(new_c)

@app.route('/clients/<id>', methods=['PUT'])
def mod_client(id):
    client = Clients.query.get(id)
    client.name = request.json['name']
    client.address = request.json['address']
    client.contact = request.json['contact']
    client.telephone = request.json['telephone']
    db.session.commit()
    return client_schema.jsonify(client)

@app.route('/products', methods=['GET'])
def get_products():
    all_prods = Products.query.all()
    result = prods_schema.dump(all_prods)
    return jsonify(result)

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    prod = Products.query.get(id)
    return prod_schema.jsonify(prod)

@app.route('/products', methods=['POST'])
def add_product():
    name = request.json['name']
    quantity = request.json['quantity']
    price = request.json['price']
    description = request.json['description']
    new_p = Products(name,quantity,price,description)
    db.session.add(new_p)
    db.session.commit()
    return prod_schema.jsonify(new_p)

@app.route('/products/<id>', methods=['PUT'])
def mod_prod(id):
    prod = Products.query.get(id)
    prod.name = request.json['name']
    prod.quantity = request.json['quantity']
    prod.price = request.json['price']
    prod.description = request.json['description']
    db.session.commit()
    return prod_schema.jsonify(prod)

if __name__ == "__main__":
    app.run(debug=True)
# --------------------- Jeyson Antonio Flores Deras --- August 2020 ------------------------------