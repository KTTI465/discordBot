import configparser
import os

class AllowUser():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./env/allow_user.ini', 'UTF-8')

    def allow_user(self) -> dict:
        return dict(self.config['USERID'])
    
    def user_auth(self, userId:int):
        return str(userId) in self.allow_user().values()
    
    def add_user(self, user_name:str, user_id:int):
        self.config.set('USERID', user_name, str(user_id))

        with open('./env/allow_user.ini', 'w') as f:
            self.config.write(f)