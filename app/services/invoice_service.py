from flask import Blueprint, request, jsonify
from app.models.invoice_model import InvoiceModel

invoice_model = InvoiceModel()


class InvoiceService:

    def __init__(self):
        self.invoice_view = self.invoice_routes()

    def invoice_routes(self):
        invoice_views = Blueprint("invoice_views", __name__)

        # Invoice Route
        # add new invoice
        @invoice_views.route("/add_invoice", methods=["POST"])
        def add_invoice():
            try:
                data = request.json
                response = invoice_model.add_invoice(**data)
                return jsonify(response)
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})

        # get all invoices
        @invoice_views.route("/invoices", methods=["GET"])
        def get_invoices():
            try:
                response = invoice_model.get_invoices()
                if response:
                    return jsonify({"statusCode": 200, "data": response})
                else:
                    return jsonify({"statusCode": 404, "errorType": "Invoices not found"})
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})

        # get selected invoice
        @invoice_views.route("/invoices/<int:invoice_id>", methods=["GET"])
        def get_invoice(invoice_id):
            try:
                if invoice_id:
                    response = invoice_model.get_invoice(invoice_id=invoice_id)
                    if response:
                        return jsonify({"statusCode": 200, "data": response})
                    else:
                        return jsonify({"statusCode": 404, "errorType": "Invoice is not found"})
                else:
                    return jsonify({"statusCode": 400, "errorType": "Invalid invoice"})
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})

        # delete selected invoice
        @invoice_views.route("/invoices/<int:invoice_id>", methods=["DELETE"])
        def remove_invoice(invoice_id):
            try:
                if invoice_id:
                    response = invoice_model.delete_invoice(invoice_id=invoice_id)
                    if response:
                        return jsonify({"statusCode": 200, "data": response})
                    else:
                        return jsonify({"statusCode": 404, "errorType": "Invoice not found"})
                else:
                    return jsonify({"statusCode": 400, "errorType": "Invalid invoice"})
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})

        # get customer and invoice based on given customer id
        @invoice_views.route("/invoice/<int:customer_id>", methods=["GET"])
        def get_customer_and_invoice(customer_id):
            try:
                if customer_id:
                    response = invoice_model.get_invoice_and_customer(customer_id)
                    if response:
                        return jsonify({"statusCode": 200, "data": response})
                    else:
                        return jsonify({"statusCode": 404, "errorType": "Customer and Invoice not found"})
                else:
                    return jsonify({"statusCode": 400, "errorType": "Invalid customer"})
            except:
                return jsonify({"statusCode": 500, "errorText": "Internal server error"})

        return invoice_views
