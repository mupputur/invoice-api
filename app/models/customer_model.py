from app.libUtils.db_connect import DbInterface
from app.libUtils.db_config import read_config

# read from config file and pass database credentials
config = read_config()
print(config["db_host"], config["db_user"], config["db_pwd"])
my_db = DbInterface(db_host=config["db_host"], db_user=config["db_user"], db_pwd=config["db_pwd"])


class CustomersModel:
    def __init__(self):
        pass

    def add_customer(self, **kwargs):
        try:
            first_name = kwargs.get('first_name')
            last_name = kwargs.get('last_name')
            company = kwargs.get('company')
            gender = kwargs.get('gender')
            city = kwargs.get('city')
            country = kwargs.get('country')
            postal_code = kwargs.get('postal_code')
            email = kwargs.get('email')
            phone = kwargs.get('phone')

            # check if the customer already exists
            filter_customer = f''' SELECT Email FROM tb_customer WHERE Email LIKE '%{email}%' '''

            # execute sql query to filter the customer
            my_db.db_cursor.execute(filter_customer)
            existing_customer = my_db.db_cursor.fetchone()

            if existing_customer:
                print(f"Customer already exists with {email}")
                return f"Customer already exists with {email}"
            else:
                # add new customer
                insert_query = '''INSERT INTO tb_customer
                                (FirstName, LastName, Company, Gender, City, Country, PostalCode, Email, Phone)
                                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                insert_data = (first_name, last_name, company, gender, city, country, postal_code, email, phone)

                # execute sql query to insert new record
                my_db.db_cursor.execute(insert_query, insert_data)
                #my_db.commit()
                my_db.commit_changes()
                return f"Customer {first_name} {last_name} added successfully"
        except Exception as e:
            print("something went wrong")
            return e

    def get_customers(self):
        try:
            select_query = '''SELECT * FROM tb_customer'''
            # execute sql query to fetch all customers
            my_db.db_cursor.execute(select_query)
            all_customers = [dict((my_db.db_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                             my_db.db_cursor.fetchall()]
            if all_customers:
                return all_customers
            else:
                return None
        except Exception as e:
            return e

    def get_customer(self, customer_id):
        try:
            select_query = f"SELECT * FROM tb_customer WHERE CustomerID = '{customer_id}'"

            # execute sql query to fetch selected customer
            my_db.db_cursor.execute(select_query)
            customer = None
            customer = [dict((my_db.db_cursor.description[i][0], value) for i, value in enumerate(row)) for row in \
                        my_db.db_cursor.fetchall()]
            if customer:
                return customer
            else:
                return customer
        except Exception as e:
            print("error", e)
            return e

    def delete_customer(self, customer_id):
        try:
            # check if the customer exists or not
            filter_customer = f''' SELECT Email FROM tb_customer WHERE CustomerId LIKE '%{customer_id}%' '''

            # execute sql query to filter the customer
            my_db.db_cursor.execute(filter_customer)
            existing_customer = my_db.db_cursor.fetchall()
            if existing_customer:
                delete_query = f"DELETE FROM tb_customer WHERE CustomerID = '{customer_id}'"

                # execute sql query to delete customer based on given customer id
                my_db.db_cursor.execute(delete_query)
                #my_db.commit()
                my_db.commit_changes()
                return f"CustomerID: {customer_id} deleted"
            else:
                return None
        except Exception as e:
            return e


