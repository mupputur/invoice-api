from flask import Flask

app = Flask(__name__)

from app.services.customer_view import *
from app.services.invoice_view import *

if __name__ == "__main__":
    app.run()
