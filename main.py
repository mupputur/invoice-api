from flask import Flask

app = Flask(__name__)

from app.services.customer_service import CustomerService
from app.services.invoice_service import InvoiceService

customer_view = CustomerService()
invoice_view = InvoiceService()

app.register_blueprint(customer_view.customer_view)
app.register_blueprint(invoice_view.invoice_view)

if __name__ == "__main__":
    app.run()
