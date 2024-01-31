import configparser
import os

class Config():
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(path, 'UTF-8')

    @property
    def token(self) -> str:
        return str(self.config['TOKEN']['TOKEN'])
    
    @property
    def mailaddress(self) -> str:
        return str(self.config['MAILADDRESS']['MAILADDRESS'])
    
    @property
    def mailpassword(self) -> str:
        return str(self.config['MAILPASS']['MAILPASS'])
    
    @property
    def adminpassword(self) -> str:
        return str(self.config['ADMINPASS']['ADMINPASS'])