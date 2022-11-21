from config import config
import mysql.connector

# get config
config = config.read_config()


class DbConnection:

    def db_connection(self):
        try:
            my_db = mysql.connector.connect(
                host=config["db_host"],
                user=config["db_user"],
                password=config["db_pwd"],
                database=config["db_name"]
            )
            if my_db:
                print("connected database")
            return my_db
        except Exception as e:
            print("Exception: ", e)


#my_db = DbConnection().db_connection()
