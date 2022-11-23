from flask import Blueprint, request, jsonify, abort
from app.models.customer_model import CustomersModel

customer_model = CustomersModel()


class CustomerService:

    def __init__(self):
        self.customer_view = self.customer_routes()

    def customer_routes(self):
        customer_views = Blueprint("customer_views", __name__)

        @customer_views.route("/", methods=["GET", "POST"])
        def home():
            return "<h1>Hello Team<h1>"

        # add new customer
        @customer_views.route("/add_customer", methods=["POST"])
        def add_customer():
            data = request.json
            response = customer_model.add_customer(**data)
            return jsonify(response)

        # get all customers
        @customer_views.route("/customers", methods=["GET"])
        def get_customers():
            response = customer_model.get_customers()
            return jsonify(customers=response)

        # get selected customer
        @customer_views.route("/customers/<int:customer_id>", methods=["GET"])
        def get_customer(customer_id):
            response = customer_model.get_customer(customer_id=customer_id)
            if len(response) != 0:
                return jsonify(customer=response)
            else:
                abort(404, description=f"CustomerID: {customer_id} not found, Please try with other search criteria")

        # delete selected customer
        @customer_views.route("/customers/<int:customer_id>", methods=["DELETE"])
        def remove_customer(customer_id):
            response = customer_model.delete_customer(customer_id=customer_id)
            print("res", response)
            if response:
                return jsonify(customer=response)
            else:
                abort(404, description=f"CustomerID: {customer_id} not found, Please try with other search criteria")
        return customer_views

'''
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
    if len(response) != 0:
        return jsonify(customer=response)
    else:
        abort(404, f"CustomerID: {customer_id} is not exist, Please try with other search criteria")


# delete selected customer
@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def remove_customer(customer_id):
    response = customer_model.delete_customer(customer_id=customer_id)
    if response:
        return jsonify(customer=response)
    else:
        abort(404, f"CustomerID: {customer_id} is not exist, Please try with other search criteria")
'''