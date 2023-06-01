import pandas as pd
from tweet_db import TweetDb as db

# Extract data from the source
def extract_data():

    # check the last record from twitter_raw inserted into clean tables
    latest_tweetid = db.select_table(table='tweets', columns=['tweet_id'], latest=True, latest_id='id')
    last_pk = db.select_table(table='twitter_raw', columns=['pk'], where='tweet_id =' + str(latest_tweetid), latest=True, latest_id='pk')

    if last_pk == "":
        last_pk = 0

    raw_tables = db.select_table(table='twitter_raw', where='pk >' + str(last_pk))
    
    return pd.DataFrame(raw_tables)

# Transform data
def transform_data(df):

    return

# Load data into the destination
def load_data(df):

    ### users_table
    userid_db =  db.select_table(table='users', columns=['user_id']) 

    if user_id in userid_db:
        
        #check if user is existing in users table

        columns = ['user_description', 'user_followers']

        old_row = db.select_table(table='users', columns=columns, where='user_id=' + str(user_id))
        new_row = db.select_table(table='twitter_raw', columns=columns, where='user_id=' + str(user_id), latest=true)

        def check_lists_equal(list1, list2):
            if len(list1) != len(list2):
                return False

            for value1, value2 in zip(list1, list2):
                if value1 != value2:
                    return False
            return True

        if not check_lists_equal(old_row,new_row):
            update_table(table='users', columns=columns, values=new_row, where='user_id=' + str(userid))	
    else:
        insert_into_users()




# Main ETL function
def etl_process():
    # Extract data from the source
    extracted_data = extract_data()

    # Transform the data
    transformed_data = transform_data(extracted_data)

    # Load the transformed data into the destination
    load_data(transformed_data)

# Execute the ETL process
etl_process()
