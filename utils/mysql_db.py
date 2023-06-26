
import pymysql
import os 

from utils.credentials import Credentials
from utils.constants import LOCAL_ENV, LOCAL_DB, CI_ENV, DEPLOY_ENV

ENV = os.getenv('ENV')

class MySQLDB:

    def __init__(self,cursorclass='', *args, **kwargs):

        if ENV == CI_ENV or ENV == DEPLOY_ENV:
            self.db = pymysql.connect(
                host=os.getenv('DB_HOST', ''),
                user=os.getenv('DB_USER', ''),
                password=os.getenv('DB_PASS', ''),
                database=os.getenv('DB_NAME', ''),
                port=int(os.getenv('DB_PORT', 0)) or 0,
            )
        else:
            cred = Credentials().database(LOCAL_DB)
            self.db = pymysql.connect(
                host=cred["DB_HOST"],
                user=cred["DB_USER"],
                password=cred["DB_PASS"],
                database=cred["DB_NAME"],
                port=cred["DB_PORT"],
                cursorclass=self.__set_cursorclass(cursorclass)                
            )

    def __set_cursorclass(self, cursorclass):
        if cursorclass == 'dict':
            return pymysql.cursors.DictCursor
        else:
            return pymysql.cursors.Cursor

    def execute_query(self, query:str, is_fetchall=True, is_get_cursor=False):

        with self.db.cursor() as cursor:

            cursor.execute(query)
            if is_get_cursor:
                return cursor

            if is_fetchall:
                return cursor.fetchall()
            return cursor.fetchone()

    def rollback(self):
        # Rollback the transaction if an error occurs
        self.db.rollback()

    def execute_many(self, query:str, values:list):

        with self.db.cursor() as cursor:
            cursor.executemany(query, values)


    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()