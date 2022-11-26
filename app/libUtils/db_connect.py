from app.libUtils import db_config
import mysql.connector

# get config
config = db_config.read_config()


class DbConnection:

    def connect(self):
        try:
            print(config["db_host"])
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




