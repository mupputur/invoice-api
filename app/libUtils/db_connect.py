import mysql.connector
from mysql.connector import errorcode


class DbInterface:

    DB_NAME = "invoiceDB"

    TABLES = {}

    TABLES['tb_customer'] = """
        CREATE TABLE tb_customer (
        CustomerId INT NOT NULL AUTO_INCREMENT,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        Company VARCHAR(16) NOT NULL,
        gender ENUM('M','F') NOT NULL,
        City VARCHAR(50) NOT NULL,
        Country VARCHAR(50) NOT NULL,
        PostalCode INT NOT NULL,
        Email VARCHAR(50) NOT NULL,
        PRIMARY KEY (CustomerId)
        ) ENGINE=InnoDB;
        """

    TABLES['tb_invoices'] = """
    CREATE TABLE tb_invoices (
        InvoiceId INT NOT NULL,
        CustomerId INT NOT NULL,
        InvoiceDate DATE NOT NULL,
        BillingAddress VARCHAR(50) NOT NULL,
        BillingCity VARCHAR(50) NULL,
        BillingState VARCHAR(50) NULL,
        BillingPostalCode INT NOT NULL,
        PRIMARY KEY (InvoiceId)
        )ENGINE=InnoDB;
    """

    def __init__(self, **kwargs):
        """
        Initializing the connection parameters
        Created the db and tables incase if its not exits
        """
        self.user = kwargs.get("db_user")
        self.password = kwargs.get("db_pwd")
        self.host = kwargs.get("db_host")
        self.con = None
        self.db_cursor = None
        self.initialize_db()

    @classmethod
    def create_database(cls, cursor):
        """
        Creates the database
        """
        try:
            cursor.execute(
                    "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(cls.DB_NAME))
        except mysql.connector.Error as err:
                print("Failed creating database: {}".format(err))
                exit(1)

    def connect(self):
        """
        This method connects the database and returns the cursor object
        """
        try:
            self.con = mysql.connector.connect(host=self.host,
                                               user=self.user,
                                               password=self.password)
            self.db_cursor = self.con.cursor()
        except Exception as e:
            print(f"Unable to connect to the data base. {str(e)}")
            exit(1)

    def initialize_db(self):
        """
        Initializes the database and the tables
        """
        self.connect()
        try:
            self.db_cursor.execute("USE {}".format(DbInterface.DB_NAME))
            print("Database {}  exists.".format(DbInterface.DB_NAME))
            self.create_tables()
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DbInterface.DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                # Creating a database if not exits
                DbInterface.create_database(self.db_cursor)
                print("Database {} created successfully.".format(DbInterface.DB_NAME))
                self.db_cursor.execute("USE {}".format(DbInterface.DB_NAME))
                self.create_tables()
                self.con.database = DbInterface.DB_NAME
            else:
                print(err)
                exit(1)

    def create_tables(self):
        """
        Initializes all tables headers were defined
        """
        tables = DbInterface.TABLES
        for table_name in tables:
            table_description = tables[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.db_cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        # self.db_cursor.close()
        # self.con.close()

    def commit_changes(self):
        if self.con:
            self.con.commit()

if __name__ == "__main__":
    db = DbInterface(db_host="127.0.0.1", db_user="root", db_pwd="Siva@123")