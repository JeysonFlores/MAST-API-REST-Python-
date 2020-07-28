from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uwu:password@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    address = db.Column(db.String(40))

    def __init__(self,name,address):
        self.name = name
        self.address = address

db.create_all()

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id','name','address')

emp_schema = EmployeeSchema()
emps_schema = EmployeeSchema(many=True)

@app.route('/employees', methods=['POST'])
def new_emp():
    name = request.json['name']
    address = request.json['address']
    new_e = Employee(name,address)
    db.session.add(new_e)
    db.session.commit()
    return emp_schema.jsonify(new_e)

#@app.route('/employees', methods=['GET']):

if __name__ == "__main__":
    app.run(debug=True)
    