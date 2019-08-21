import requests
from requests.exceptions import ConnectionError
from lxml import html
import logging
from traceback import format_exc
from pdb import set_trace
import os
import pandas as pd
import re

from db_utlity import SQlAlchemyOperation,MysqlConn
import constants

schema_name="web_address_lookup"

#for dumping the data
sql_obj=SQlAlchemyOperation()
web_address_lookup_table_conn=sql_obj.get_sqlalchemy_conn(database_name="web_address_lookup")

#to get the result of the query in the form of dataframe
pymysql_obj=MysqlConn()
conn=pymysql_obj.pymysql_connect()

logging.basicConfig(filename=f'{constants.dt_time}_output.log',filemode='w',level=logging.INFO,format=constants.LOG_FORMAT)

class Operation(object):
    def __init__(self):
        pass

    def get_data(self,*args,**kwargs):
        pass

    def load_data(self,*args,**kwargs):
        pass


class InputOperation(Operation):
    """
    2. Create a python script that takes the file path of the attached CSV 
    and loads the CSV into web_address_lookup.address_input.
    """
    table_name="address_input"

    def __init__(self):
        pass
    
    def get_data(self,filename="address_lookup_table.csv"):
        df=pd.read_csv(filename)
        return df

    def load_data(self,df="",dbaction=""):
        """

        How to behave if the table already exists with 'dbaction'.
        fail: Raise a ValueError.
        replace: Drop the table before inserting new values.
        append: Insert new values to the existing table.
        """
        sql_obj.append_db(df,conn=web_address_lookup_table_conn,tabl_name=table_name,schema=schema_name,action=dbaction)

    def update_data(self,conn="",address_id=[]):
        """
        UPDATE web_address_lookup.address_input.needs_lookup to zero.
        """
        try:
            cursor = conn.cursor()
            for i in address_id:
                cursor.execute(constants.updatequery_address_input, str(address_id))
        except Exception as error:
            print(error)

        finally:
            conn.commit()
            print("success")
            cursor.close()
            conn.close()        
        

class OutputOperation(Operation):

    table_name="address_output"

    def __init__(self):
        pass

    def get_data(self):
        df=pd.DataFrame(columns=["address_id", "http_response_code", "redirected_to_url", "html", "lookup_timestamp"])
        df["lookup_timestamp"]=constants.now_time
        return df

    def load_data(self,df,dbaction=""):
        """
        How to behave if the table already exists with 'dbaction'.
        fail: Raise a ValueError.
        replace: Drop the table before inserting new values.
        append: Insert new values to the existing table.
        """
        sql_obj.append_db(df,conn=web_address_lookup_table_conn,tabl_name=table_name,schema=schema_name,action=dbaction)
    
    def get_status_code(self,x):
        try:
            print(x)
            pattern=r'^3+'
            txt=str(requests.get(x).status_code)
            if re.findall(pattern,txt) !=[]:
                print(x)
            return txt
        except ConnectionError as ce:
            print(ce)
            return "503"
        except:
            print("Exception in",x)
            return "503"

    def get_html(self,x):
        try:
            print(x)
            txt=str(requests.get(x).text)
            return txt
        except ConnectionError as ce:
            print(ce)
            return "Not found"
        except:
            print("Exception in",x)
            return "Not found"

    def get_redirected_url(self,df):
        txt=df[df['status']>='300' & df['status']<'400']
        df['redirected_to_url']=(txt)
    
    def set_data(self,df_input):
        df_input['status']=df_input['url'].apply(self.find_300)
        return df_input

    def temp_operation(self,df):
        df['url']="http://"+df.web_address
        df['status']=" "
        return df
    

if __name__=="__main__":
    ...

