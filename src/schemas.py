from __main__ import ma

class EmployeesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'email', 'telephone', 'job', 'gender', 'status')


class ClientsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'contact', 'telephone', 'status')


class ProductsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'quantity', 'price', 'description', 'status')