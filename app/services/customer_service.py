from flask import Blueprint, request, jsonify
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
            try:
                data = request.json
                response = customer_model.add_customer(**data)
                return jsonify(response)
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})

        # get all customers
        @customer_views.route("/customers", methods=["GET"])
        def get_customers():
            try:
                response = customer_model.get_customers()
                if response:
                    return jsonify({"statusCode": 200, "data": response})
                else:
                    return jsonify({"statusCode": 404, "errorType": "Customers not found"})
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})

        # get selected customer
        @customer_views.route("/customers/<int:customer_id>", methods=["GET"])
        def get_customer(customer_id):
            try:
                if customer_id:
                    response = customer_model.get_customer(customer_id=customer_id)
                    if response:
                        return jsonify({"statusCode": 200, "data": response})
                    else:
                        return jsonify({"statusCode": 404, "errorType": "Customer is not found"})
                else:
                    return jsonify({"statusCode": 400, "errorType": "Invalid customer"})
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})

        # delete selected customer
        @customer_views.route("/customers/<int:customer_id>", methods=["DELETE"])
        def remove_customer(customer_id):
            try:
                if customer_id:
                    response = customer_model.delete_customer(customer_id=customer_id)
                    if response:
                        return jsonify({"statusCode": 200, "data": response})
                    else:
                        return jsonify({"statusCode": 404, "errorType": "Customer not found"})
                else:
                    return jsonify({"statusCode": 400, "errorType": "Invalid customer"})
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})
        return customer_views

