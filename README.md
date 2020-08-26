# MAST-API-Rest

![Screenshot](https://github.com/JeysonFlores/MAST-API-Rest/blob/master/resources/MAST_Logo.png)


# Documentation 
 <h3> Routes </h3>
  
  |Token Required | Method | Route | Description |
  | ----- | ----- | ----- | ---------|
  |✔|POST|/signup|Send a JSON object with the new user information|
  |uwu|GET|/login|Send a JSON object with user & password and returns the sesssion token|
  |✔|GET|/about|Return all the API's development information|
  |✔|GET|/stats|Return the on-run API's stats|
  |✔|GET|uwu|uwu|
  |✔|GET|uwu|uwu|
  |✔|uwu|uwu|uwu|
  |✔|uwu|uwu|uwu|
  
  - [POST] /signup ---------------- Send a JSON object with the new user information
  - [GET] /login ---------------------------   Send a JSON object with user & password and returns the sesssion token
  - [TOKEN_REQUIRED][GET] /about -------------------------   Return all the API's development information
  - [TOKEN_REQUIRED][GET] /stats -------------------------   Return the on-run API's stats
  - [TOKEN_REQUIRED][GET] /employees  --------------------   Return all the employees on the database
  - [TOKEN_REQUIRED][GET] /employees/_id_ ----------------   Return the specified employee's information
  - [TOKEN_REQUIRED][POST] /employees ----------   Send a JSON object with the employee's information to save
  - [TOKEN_REQUIRED][PUT] /employees/_id_ -------  Send a JSON object with the specified employee's information to update
  - [TOKEN_REQUIRED][GET] /clients  --------------------   Return all the clients on the database
  - [TOKEN_REQUIRED][GET] /clients/_id_ ----------------   Return the specified client's information
  - [TOKEN_REQUIRED][POST] /clients --------------------   Send a JSON object with the client's information to save
  - [TOKEN_REQUIRED][PUT] /clients/_id_-------  Send a JSON object with the specified client's information to update
  - [TOKEN_REQUIRED][GET] /products  --------------------   Return all the products on the database
  - [TOKEN_REQUIRED][GET] /products/_id_ ----------------   Return the specified product's information
  - [TOKEN_REQUIRED][POST] /products ----------------   Send a JSON object with the product's information to save
  - [TOKEN_REQUIRED][PUT] /products/_id_ -------  Send a JSON object with the specified product's information to update
 
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
