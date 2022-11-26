import json


# read config file
def read_config():
    try:
        filename = 'app/config/config.json'
        config_file = open(filename, 'r')
        config = json.load(config_file)
        config_file.close()
        return config
    except Exception as e:
        print("Exception: ", filename)
