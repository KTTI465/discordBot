import sqlite3
import secrets

class DBMS():
    def __init__(self):
        authDB = sqlite3.connect('./database/auth.db')
        roleDB = sqlite3.connect()
        authCur = authDB.cursor()
        #create table
        authCur.execute(
            'CREATE TABLE IF NOT EXISTS User(user_id INTEGER PRIMARY KEY, user_name STRING, verify INTEGER, token STRING)'
        )
        authDB.close()

    def get_token(self, user_id:int):
        authDB = sqlite3.connect('./database/auth.db')
        authCur = authDB.cursor()
        data = authCur.execute(
            'SELECT token FROM User WHERE user_id = ?', (user_id,)
        ).fetchone()
        authDB.close()

        if data != None:
            return data[0]
        else:
            return None


    def set_token(self, user_id:int, user_name:str):
        authDB = sqlite3.connect('../database/auth.db')
        authCur = authDB.cursor()
        data = authCur.execute(
            'SELECT * FROM User WHERE user_id = ?', (user_id,)
        ).fetchone()

        if data != None:
            return False
        else:
            authCur.execute(
                'INSERT INTO User (user_id, user_name, verify, token) VALUES (?, ?, ?, ?)', (user_id, user_name, 0, secrets.token_hex(2))
            )
            authDB.commit()
        authDB.close()
        return True
    
    def auth_token(self, user_id:int, token:str):
        token_db = self.get_token(user_id=user_id)

        if token_db == None:
            return "Notfound"
        
        if token == str(token_db):
            authDB = sqlite3.connect('./database/auth.db')
            authCur = authDB.cursor()
            data = authCur.execute(
                'SELECT verify FROM User WHERE user_id = ?', (user_id,)
            ).fetchone()
            if data[0] != 1:
                authCur.execute(
                    'UPDATE User SET verify = 1 WHERE user_id = ?', (user_id,)
                )
                authDB.commit()
                authDB.close()
                return "Success"
            else:
                authDB.close()
                return "Already"
            
        else:
            return "Faild"
        
    