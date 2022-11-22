import json


# read config file
def read_config():
    try:
        with open("config/config.json", "rb") as config_file:
            config = json.load(config_file)
            return config
    except Exception as e:
        print("Exception: ", e)
