from app.main import app
from flask import request, jsonify
from app.models.invoice_model import InvoiceModel

invoice_model = InvoiceModel()


# Invoice Route
# add new invoice
@app.route("/add_invoice", methods=["POST"])
def add_invoice():
    data = request.json
    response = invoice_model.add_invoice(**data)
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
