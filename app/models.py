from db_config import DbConnection

my_db = DbConnection().db_connection()
my_cursor = my_db.cursor()


class CustomersModel:
    def add_customer(self, customer_id, first_name, last_name, company, address, city, state, country, postal_code, phone, email):
        # check if the customer already exists
        filter_customer = f''' SELECT Email FROM customer WHERE Email LIKE '%{email}%' '''

        # execute sql query to filter the customer
        my_cursor.execute(filter_customer)
        existing_customer = my_cursor.fetchone()

        if existing_customer:
            print(f"Customer already exists with {email}")
            return f"Customer already exists with {email}"
        else:
            # add new customer
            insert_query = '''INSERT INTO customer
                            (CustomerId, FirstName, LastName, Company, Address, City, State, Country, 
                            PostalCode, Phone, Email)
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            insert_data = (customer_id, first_name, last_name, company, address, city, state, country, postal_code, phone, email)

            # execute sql query to insert new record
            my_cursor.execute(insert_query, insert_data)
            my_db.commit()
            print(f"Customer {first_name} {last_name} added successfully")
            return f"Customer {first_name} {last_name} added successfully"

    def get_customers(self):
        select_query = '''SELECT * FROM customer'''

        # execute sql query to fetch all customers
        my_cursor.execute(select_query)
        all_customers = [dict((my_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                         my_cursor.fetchall()]
        print("customers: ", all_customers)
        return all_customers

    def get_customer(self, customer_id):
        select_query = f"SELECT * FROM customer WHERE CustomerID = '{customer_id}'"

        # execute sql query to fetch selected customer
        my_cursor.execute(select_query)
        customer = None
        customer = [dict((my_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                    my_cursor.fetchall()]
        if customer:
            print("customer: ", customer)
            return customer
        else:
            print("Something went wrong try with other search criteria")
            return customer

    def delete_customer(self, customer_id):
        # check if the customer exists or not
        filter_customer = f''' SELECT Email FROM customer WHERE CustomerId LIKE '%{customer_id}%' '''

        # execute sql query to filter the customer
        my_cursor.execute(filter_customer)
        existing_customer = my_cursor.fetchone()

        if existing_customer:
            delete_query = f"DELETE FROM customer WHERE CustomerID = '{customer_id}'"

            # execute sql query to delete customer based on given customer id
            my_cursor.execute(delete_query)
            my_db.commit()
            print(f"Deleted {customer_id}")
            return f"CustomerID: {customer_id} deleted"
        else:
            print(f"CustomerID {customer_id} doesn't exist")
            return f"CustomerID {customer_id} doesn't exist"



class InvoiceModel:
    def add_invoice(self, invoice_id, customer_id, invoice_date, billing_address, billing_city,
                    billing_state, billing_country, billing_postal_code, total):
        # add new customer
        insert_query = '''INSERT INTO invoice
                        (InvoiceId, CustomerId, InvoiceDate, BillingAddress, BillingCity, 
                        BillingState, BillingCountry, BillingPostalCode, Total)
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        insert_data = (invoice_id, customer_id, invoice_date, billing_address, billing_city,
                       billing_state, billing_country, billing_postal_code, total)

        # execute sql query to insert new record
        my_cursor.execute(insert_query, insert_data)
        my_db.commit()
        print(f"Invoice {invoice_id} added successfully")
        return f"Invoice {invoice_id} added successfully"

    def get_invoices(self):
        select_query = '''SELECT * FROM invoice'''

        # execute sql query to fetch all customers
        my_cursor.execute(select_query)
        all_invoices = [dict((my_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                         my_cursor.fetchall()]
        print("customers: ", all_invoices)
        return all_invoices

    def get_invoice(self, invoice_id):
        select_query = f"SELECT * FROM invoice WHERE InvoiceId = '{invoice_id}'"

        # execute sql query to fetch selected customer
        my_cursor.execute(select_query)
        invoice = None
        invoice = [dict((my_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                    my_cursor.fetchall()]
        if invoice:
            print("invoice: ", invoice)
            return invoice
        else:
            print("Something went wrong try with other search criteria")
            return invoice

    def delete_invoice(self, invoice_id):
        # check if the invoice exists or not
        filter_customer = f''' SELECT Email FROM invoice WHERE InvoiceId LIKE '%{invoice_id}%' '''

        # execute sql query to filter the invoice
        my_cursor.execute(filter_customer)
        existing_invoice = my_cursor.fetchone()
        if existing_invoice:
            delete_query = f"DELETE FROM invoice WHERE InvoiceId = '{invoice_id}'"

            # execute sql query to delete customer based on given customer id
            my_cursor.execute(delete_query)
            my_db.commit()
            print(f"Invoice: {invoice_id} deleted")
            return f"Invoice: {invoice_id} deleted"
        else:
            print(f"InvoiceID {invoice_id} doesn't exist")
            return f"InvoiceID {invoice_id} doesn't exist"

    def get_invoice_and_customer(self, customer_id):
        select_query = f'''SELECT C.CustomerId, C.FirstName, C.LastName, C.Company, C.Address, C.City, C.State, 
            C.Country, C.PostalCode, C.Phone, C.Email, I.InvoiceId, I.InvoiceDate, I.BillingAddress,
            I.BillingCity, I.BillingState, I.BillingCoUntry, I.BillingPostalCode, I.Total
            FROM flaskdb.customer AS C INNER JOIN flaskdb.invoice AS I ON I.CustomerId = C.CustomerId
            WHERE C.CustomerId = {customer_id}'''

        # execute sql query to fetch selected customer and invoice
        my_cursor.execute(select_query)
        customer_invoice = None
        customer_invoice = [dict((my_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                            my_cursor.fetchall()]

        if customer_invoice:
            print("customer&invoice: ", customer_invoice)
            return customer_invoice
        else:
            print("Something went wrong try with other search criteria")
            return customer_invoice


# CustomersModel().add_customer(first_name="Manohar", last_name="Upputuri", company="Apple", address="USA", city="USA", \
#                               state="USA", country="USA", postal_code=54553, phone=3332222111, email="manohar@gmail.com")
#
# CustomersModel().get_customer(customer_id=4)
#CustomersModel().delete_customer(customer_id=2)


# InvoiceModel().add_invoice(invoice_id=1234, customer_id=1002, invoice_date="01-01-2022", billing_address="USA", billing_city="USA",
#                     billing_state="USA", billing_country="USA", billing_postal_code=1122, total=10000)
# InvoiceModel().get_invoices()
# InvoiceModel().get_invoice(invoice_id=1234)
# InvoiceModel().delete_invoice(invoice_id=1234)
InvoiceModel().get_invoice_and_customer(customer_id=102)

