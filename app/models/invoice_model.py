from app.libUtils.db_connect import DbInterface
from app.libUtils.db_config import read_config

# read from config file and pass database credentials
config = read_config()

my_db = DbInterface(db_host=config["db_host"], db_user=config["db_user"], db_pwd=config["db_pwd"])


class InvoiceModel:
    def __init__(self):
        pass

    def add_invoice(self, **kwargs):
        try:
            invoice_id = kwargs.get('invoice_id')
            customer_id = kwargs.get('customer_id')
            invoice_date = kwargs.get('invoice_date')
            billing_address = kwargs.get('billing_address')
            billing_city = kwargs.get('billing_city')
            billing_state = kwargs.get('billing_state')
            billing_postal_code = kwargs.get('billing_postal_code')
            # add new customer
            insert_query = '''INSERT INTO tb_invoices
                            (InvoiceId, CustomerId, InvoiceDate, BillingAddress, BillingCity,
                            BillingState, BillingPostalCode)
                            VALUES(%s, %s, %s, %s, %s, %s, %s)'''
            insert_data = (invoice_id, customer_id, invoice_date, billing_address, billing_city,
                           billing_state, billing_postal_code)

            # execute sql query to insert new record
            my_db.db_cursor.execute(insert_query, insert_data)
            my_db.commit_changes()
            return f"Invoice {invoice_id} added successfully"
        except Exception as e:
            print("something went wrong")
            return e

    def get_invoices(self):
        try:
            select_query = '''SELECT * FROM tb_invoices'''

            # execute sql query to fetch all customers
            my_db.db_cursor.execute(select_query)
            all_invoices = [dict((my_db.db_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                             my_db.db_cursor.fetchall()]
            if all_invoices:
                return all_invoices
            else:
                return None
        except Exception as e:
            return e

    def get_invoice(self, invoice_id):
        try:
            select_query = f"SELECT * FROM tb_invoices WHERE InvoiceId = '{invoice_id}'"

            # execute sql query to fetch selected customer
            my_db.db_cursor.execute(select_query)
            invoice = None
            invoice = [dict((my_db.db_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                        my_db.db_cursor.fetchall()]
            if invoice:
                return invoice
            else:
                return invoice
        except Exception as e:
            return e

    def delete_invoice(self, invoice_id):
        try:
            # check if the invoice exists or not
            filter_customer = f''' SELECT InvoiceId FROM tb_invoices WHERE InvoiceId LIKE '%{invoice_id}%' '''

            # execute sql query to filter the invoice
            my_db.db_cursor.execute(filter_customer)
            existing_invoice = my_db.db_cursor.fetchall()
            print(existing_invoice)
            if existing_invoice:
                delete_query = f"DELETE FROM tb_invoices WHERE InvoiceId = '{invoice_id}'"

                # execute sql query to delete customer based on given customer id
                my_db.db_cursor.execute(delete_query)
                my_db.commit_changes()
                return f"Invoice: {invoice_id} deleted"
            else:
                return None
        except Exception as e:
            return e

    def get_invoice_and_customer(self, customer_id):
        try:
            select_query = f'''SELECT C.CustomerId, C.FirstName, C.LastName, C.Company, C.Gender, C.City, 
                C.Country, C.PostalCode, C.Email, C.Phone, I.InvoiceId, I.InvoiceDate, I.BillingAddress,
                I.BillingCity, I.BillingState, I.BillingPostalCode
                FROM tb_customer AS C INNER JOIN tb_invoices AS I ON I.CustomerId = C.CustomerId
                WHERE C.CustomerId = {customer_id}'''

            # execute sql query to fetch selected customer and invoice
            my_db.db_cursor.execute(select_query)
            customer_invoice = None
            customer_invoice = [dict((my_db.db_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                                my_db.db_cursor.fetchall()]

            if customer_invoice:
                return customer_invoice
            else:
                return customer_invoice
        except Exception as e:
            return e
