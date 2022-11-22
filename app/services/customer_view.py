from flask import request, jsonify
from app.main import app
from app.models.customer_model import CustomersModel

customer_model = CustomersModel()


# Home
@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1>Hello Team<h1>"


# Customer Routes
# add new customer
@app.route("/add_customer", methods=["POST"])
def add_customer():
    data = request.json
    response = customer_model.add_customer(**data)
    return jsonify(response)


# get all customers
@app.route("/customers", methods=["GET"])
def get_customers():
    response = customer_model.get_customers()
    return jsonify(customers=response)


# get selected customer
@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    response = customer_model.get_customer(customer_id=customer_id)
    return jsonify(customer=response)


# delete selected customer
@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def remove_customer(customer_id):
    response = customer_model.delete_customer(customer_id=customer_id)
    return jsonify(response)

