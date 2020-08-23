from __main__ import db

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
