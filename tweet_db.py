
import os
import pandas as pd
from utils.constants import PROJECT_ROOT

from utils.mysql_db import MySQLDB

class TweetDb:

    def __init__(self):
        self.db = MySQLDB()
    
    def quit(self):
        self.db.close()

    def rollback(self):
        self.db.rollback()

    # SELECT TABLES 
    def select_column_names(self, table:str, exclude_increment=False):

        query = "SELECT column_name FROM information_schema.columns WHERE table_name ='" + table +"'"
        
        if exclude_increment:
            query += " AND column_name NOT IN ('pk','date_added','date_updated')"
        
        query += " ORDER BY ordinal_position"

        items = self.db.execute_query(query)
        result = [item[0] for item in items]
        #print(query)
        return result

    def select_table(self, table:str, columns=None, where=None, latest=False, latest_id='date_added'):

        if columns is not None:
            query = "SELECT " + ", ".join(columns) + " FROM " + table 
        else:
            columns = []
            query = "SELECT * FROM " + table

        if where is not None:
            query += " WHERE " + str(where)

        if latest:
            if latest_id != 'date_added':
                query += " ORDER BY " + latest_id + " DESC LIMIT 1"
            else:
                query += " ORDER BY date_added DESC LIMIT 1"
            
            items = self.db.execute_query(query)[0]
        
        else:
            items = self.db.execute_query(query)

        if len(columns) == 1:
            items = [item[0] for item in items]

        print(items)
       
    # INSERT TABLES
    def insert_table(self, table:str, values):

        columns = self.select_column_names(table=table, exclude_increment=True)

        def repeat_string(value, number):
            repeated_value = (str(value) + ',') * number
            return repeated_value[:-1]

        query = "INSERT INTO " + table + "({})".format(', '.join(columns)) + " VALUES (" + repeat_string("%s", len(columns))  + ")"

        self.db.execute_many(query, values)
        self.db.commit()

    # UPDATE TABLES
        
if __name__ == '__main__':
    
    TweetDb().select_table(table='twitter_raw', columns=['pk','tweet_id'], latest=True, latest_id='pk')
    TweetDb().select_table(table='twitter_raw', columns=['pk','tweet_id'])
    TweetDb().select_table(table='twitter_raw', columns=['username'], where='pk < 5')


