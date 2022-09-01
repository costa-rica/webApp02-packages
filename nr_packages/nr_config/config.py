import os
import json

if os.environ.get('COMPUTERNAME')=='CAPTAIN2020':
    with open(r"C:\Users\captian2020\Documents\config_files\config_whatSticks05.json") as config_file:
        config = json.load(config_file)
elif os.environ.get('COMPUTERNAME')=='NICKSURFACEPRO4':
    with open(r"C:\Users\Costa Rica\Documents\_configs\config_webApp02.json") as config_file:
        config = json.load(config_file)


class ConfigDev:
    DEBUG = True
    PORT='5000'
    SECRET_KEY = config.get('SECRET_KEY')
    SQL_URI = config.get('SQL_URI')


class ConfigProd:
    DEBUG = False
    PORT='80'
    SECRET_KEY = config.get('SECRET_KEY')
    SQL_URI = config.get('SQL_URI')
