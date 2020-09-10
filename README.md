# MAST-API-Rest

![Screenshot](https://github.com/JeysonFlores/MAST-API-Rest-Python-/blob/master/resources/MAST_Logo.png)


# Documentation 
 <h3> Routes </h3>
  
  |Token Required | Method | Route | Description |
  | ----- | ----- | ----- | ---------|
  |✘|POST|/signup|Send a JSON object with the new user information|
  |✘|GET|/login|Send a JSON object with user & password and returns the sesssion token|
  |✔|GET|/about|Return all the API's development information|
  |✔|GET|/stats|Return the on-run API's stats|
  |✔|GET|/employees|Return all the employees on the database|
  |✔|POST|/employees|Send a JSON object with the employee's information to save|
  |✔|GET|/employees/**id**|Return the specified employee's information|
  |✔|PUT|/employees/**id**|Send a JSON object with the specified employee's information to update|
  |✔|GET|/clients|Return all the clients on the database|
  |✔|POST|/clients|Send a JSON object with the client's information to save|
  |✔|GET|/clients/**id**|Return the specified client's information|
  |✔|PUT|/clients/**id**|Send a JSON object with the specified client's information to update|
  |✔|GET|/products|Return all the products on the database|
  |✔|POST|/products|Send a JSON object with the product's information to save|
  |✔|GET|/products/**id**|Return the specified product's information|
  |✔|PUT|/products/**id**|Send a JSON object with the specified product's information to update|
  
 <h3> Error Handlers </h3>
 
  -  400 Bad Request
  -  403 Forbidden
  -  404 Not Found
  -  405 Method Not Allowed
  
<h3> Security </h3>

  - Python's JSON Web Tokens Implementation
  
<h3> Resources </h3>

  - MariaDB - MySQL Server
  - WSGI Deploy Server
  - SQLAlchemy ORM
  
# Python Dependences
-  flask
-  flask_sqlalchemy
-  flask_marshmallow
-  flask-restful
-  marshmallow-sqlalchemy
-  pyjwt
-  pymysql
-  pyyaml
