from app import app
from models import CustomersModel, InvoiceModel
from flask import request, jsonify

customer_model = CustomersModel()
invoice_model = InvoiceModel()


# Home
@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1>Hello Team<h1>"


# Customer Routes
# add new customer
@app.route("/add_customer", methods=["POST"])
def add_customer():
    customer_id = request.json.get('customer_id')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    company = request.json.get('company')
    address = request.json.get('address')
    city = request.json.get('city')
    state = request.json.get('state')
    country = request.json.get('country')
    postal_code = request.json.get('postal_code')
    phone = request.json.get('phone')
    email = request.json.get('email')

    response = customer_model.add_customer(customer_id=customer_id, first_name=first_name, last_name=last_name, company=company, address=address, city=city, \
                                                   state=state, country=country, postal_code=postal_code, phone=phone, email=email)
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


# Invoice Route
# add new invoice
@app.route("/add_invoice", methods=["POST"])
def add_invoice():
    invoice_id = request.json.get('invoice_id')
    customer_id = request.json.get('customer_id')
    invoice_date = request.json.get('invoice_date')
    billing_address = request.json.get('billing_address')
    billing_city = request.json.get('billing_city')
    billing_state = request.json.get('billing_state')
    billing_country = request.json.get('billing_country')
    billing_postal_code = request.json.get('billing_postal_code')
    total = request.json.get('total')

    response = invoice_model.add_invoice(invoice_id=invoice_id, customer_id=customer_id, invoice_date=invoice_date, \
                                          billing_address=billing_address, billing_city=billing_city, billing_state=billing_state, \
                                          billing_country=billing_country, billing_postal_code=billing_postal_code, total=total)
    return jsonify(response)


# get all invoices
@app.route("/invoices", methods=["GET"])
def get_invoices():
    response = invoice_model.get_invoices()
    return jsonify(customers=response)


# get selected invoice
@app.route("/invoices/<int:invoice_id>", methods=["GET"])
def get_invoice(invoice_id):
    response = invoice_model.get_invoice(invoice_id=invoice_id)
    return jsonify(invoice=response)


# delete selected invoice
@app.route("/invoices/<int:invoice_id>", methods=["DELETE"])
def remove_invoice(invoice_id):
    response = invoice_model.delete_invoice(invoice_id=invoice_id)
    return jsonify(response)


# get customer and invoice based on given customer id
@app.route("/invoice/<int:customer_id>", methods=["GET"])
def get_customer_and_invoice(customer_id):
    response = invoice_model.get_invoice_and_customer(customer_id)
    return jsonify(CustomerAndInvoice=response)
