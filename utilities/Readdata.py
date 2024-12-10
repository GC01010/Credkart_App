import configparser
config=configparser.RawConfigParser()
config.read("..\\Configurations\\config.ini")

class Read_data:
    @staticmethod
    def login_url():
        url=config.get("application_url","login_page")
        return url

    @staticmethod
    def login_username():
        email=config.get("login_data","email")
        return email

    @staticmethod
    def login_Password():
        password = config.get("login_data", "password")
        return password