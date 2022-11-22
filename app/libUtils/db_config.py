import json


# read config file
def read_config():
    try:
        file_path = r'C:\Users\spatnayak\PythonProjects\invoice-api\app\config\config.json'
        with open(file_path, "rb") as config_file:
            config = json.load(config_file)
            return config
    except Exception as e:
        print("Exception: ", e)
