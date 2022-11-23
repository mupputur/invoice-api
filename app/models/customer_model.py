from app.libUtils.db_connect import DbConnection

my_db = DbConnection().connect()
my_cursor = my_db.cursor()


class CustomersModel:
    def __init__(self):
        pass

    def add_customer(self, **kwargs):
        customer_id = kwargs.get('customer_id')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        company = kwargs.get('company')
        address = kwargs.get('address')
        city = kwargs.get('city')
        state = kwargs.get('state')
        country = kwargs.get('country')
        postal_code = kwargs.get('postal_code')
        phone = kwargs.get('phone')
        email = kwargs.get('email')

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
        if all_customers:
            print("customers: ", all_customers)
            return all_customers
        else:
            print("No invoices data found")
            return None

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
        existing_customer = my_cursor.fetchall()
        if existing_customer:
            delete_query = f"DELETE FROM customer WHERE CustomerID = '{customer_id}'"

            # execute sql query to delete customer based on given customer id
            dd =my_cursor.execute(delete_query)
            my_db.commit()
            print(f"Deleted {customer_id}")
            return f"CustomerID: {customer_id} deleted"
        else:
            print(f"CustomerID {customer_id} doesn't exist")
            return None


# CustomersModel().add_customer(first_name="Manohar", last_name="Upputuri", company="Apple", address="USA", city="USA", \
#                               state="USA", country="USA", postal_code=54553, phone=3332222111, email="manohar@gmail.com")
#CustomersModel().get_customers()
# CustomersModel().get_customer(customer_id=4)
# CustomersModel().delete_customer(customer_id=2)
#CustomersModel().add_customer(**input)

