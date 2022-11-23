from flask import Blueprint, request, jsonify, abort
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
            data = request.json
            response = invoice_model.add_invoice(**data)
            return jsonify(response)

        # get all invoices
        @invoice_views.route("/invoices", methods=["GET"])
        def get_invoices():
            response = invoice_model.get_invoices()
            return jsonify(customers=response)

        # get selected invoice
        @invoice_views.route("/invoices/<int:invoice_id>", methods=["GET"])
        def get_invoice(invoice_id):
            response = invoice_model.get_invoice(invoice_id=invoice_id)
            if response:
                return jsonify(response)
            else:
                abort(404, description=f"InvoiceId: {invoice_id} not found, Please try with other search criteria")
            return jsonify(invoice=response)

        # delete selected invoice
        @invoice_views.route("/invoices/<int:invoice_id>", methods=["DELETE"])
        def remove_invoice(invoice_id):
            response = invoice_model.delete_invoice(invoice_id=invoice_id)
            if response:
                return jsonify(response)
            else:
                abort(404, description=f"InvoiceId: {invoice_id} not found, Please try with other search criteria")

        # get customer and invoice based on given customer id
        @invoice_views.route("/invoice/<int:customer_id>", methods=["GET"])
        def get_customer_and_invoice(customer_id):
            response = invoice_model.get_invoice_and_customer(customer_id)
            if response:
                return jsonify(CustomerAndInvoice=response)
            else:
                return jsonify({"statusCode": 404, "errorText": "Record Not Found"})
                # abort(404, description=f"CustomerID: {customer_id} not found, Please try with other search criteria")

        return invoice_views
