from __main__ import app, db, ma, emp_schema, emps_schema, client_schema, clients_schema, prod_schema, prods_schema, user_schema, Employees, Clients, Products, Users
from flask import jsonify, request, make_response
from functools import wraps
import jwt
import datetime
import secrets

app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({"error": "1", "message":"token is missing"}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({"error": "1", "message": "token is invalid"}), 403
        return f(*args,**kwargs)
    return decorated

@app.route('/login')
def login():
    user_name = request.json['name']
    user_password = request.json['password']
    user = Users.query.filter_by(name=user_name,password=user_password).first()
    if user is not None:
        token = jwt.encode({"username": user.id,"password": user.password, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=50)}, app.config['SECRET_KEY'])
        return jsonify({"token": token.decode('UTF-8')})
    return make_response(jsonify({"error": "1", "message": "Login Failed"}))

@app.route('/about')
@token_required
def about():
    return jsonify({"API": "MAST", "Version": "1.0", "Language": "Python", "Framework": "Flask", "ORM": "SQLAlchemy", "DBM": "MariaDB", "Author": "Jeyson Antonio Flores Deras"})

@app.route('/stats')
@token_required
def stats():
    return jsonify({"active-date": str(app.config['TURN_ON_TIME']), "active-time": str(datetime.datetime.utcnow() - app.config['TURN_ON_TIME'])})


@app.route('/employees', methods=['GET'])
@token_required
def get_employees():
    all_employees = Employees.query.all()
    if all_employees != []:
        result = emps_schema.dump(all_employees)
        return jsonify(result)
    return jsonify({"error": "1", "message": "there are no employees in the database"})

@app.route('/employees/<id>', methods=['GET'])
@token_required
def get_employee(id):
    emp = Employees.query.get(id)
    if emp is not None:
        return emp_schema.jsonify(emp)
    return jsonify({"error": "1", "message": "requested employee doesn't exist"})

@app.route('/employees', methods=['POST'])
@token_required
def add_employee():
    name = request.json['name']
    email = request.json['email']
    telephone = request.json['telephone']
    job = request.json['job']
    gender = request.json['gender']
    new_e = Employees(name,email,telephone,job,gender)
    db.session.add(new_e)
    db.session.commit()
    return emp_schema.jsonify(new_e)

@app.route('/employees/<id>', methods=['PUT'])
@token_required
def mod_employee(id):
    emp = Employees.query.get(id)
    if emp is not None:
        emp.name = request.json['name']
        emp.email = request.json['email']
        emp.telephone = request.json['telephone']
        emp.job = request.json['job']
        emp.gender = request.json['gender']
        db.session.commit()
        return emp_schema.jsonify(emp)
    return jsonify({"error": "1", "message": "requested employee doesn't exist"})

@app.route('/clients', methods=['GET'])
@token_required
def get_clients():
    all_clients = Clients.query.all()
    if all_clients != []:
        result = clients_schema.dump(all_clients)
        return jsonify(result)
    return jsonify({"error": "1", "message": "there are no clients in the database"})

@app.route('/clients/<id>', methods=['GET'])
@token_required
def get_client(id):
    client = Clients.query.get(id)
    if client is not None:
        return client_schema.jsonify(client)
    return jsonify({"error": "1", "message": "requested client doesn't exist"})

@app.route('/clients', methods=['POST'])
@token_required
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
@token_required
def mod_client(id):
    client = Clients.query.get(id)
    if client is not None:
        client.name = request.json['name']
        client.address = request.json['address']
        client.contact = request.json['contact']
        client.telephone = request.json['telephone']
        db.session.commit()
        return client_schema.jsonify(client)
    return jsonify({"error": "1", "message": "requested client doesn't exist"})

@app.route('/products', methods=['GET'])
@token_required
def get_products():
    all_prods = Products.query.all()
    if all_prods != []:
        result = prods_schema.dump(all_prods)
        return jsonify(result)
    return jsonify({"error": "1", "message": "there are no products in the database"})

@app.route('/products/<id>', methods=['GET'])
@token_required
def get_product(id):
    prod = Products.query.get(id)
    if prod is not None:
        return prod_schema.jsonify(prod)
    return jsonify({"error": "1", "message": "requested product doesn't exist"})

@app.route('/products', methods=['POST'])
@token_required
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
@token_required
def mod_prod(id):
    prod = Products.query.get(id)
    if prod is not None:
        prod.name = request.json['name']
        prod.quantity = request.json['quantity']
        prod.price = request.json['price']
        prod.description = request.json['description']
        db.session.commit()
        return prod_schema.jsonify(prod)
    return jsonify({"error": "1", "message": "requested product doesn't exist"})
