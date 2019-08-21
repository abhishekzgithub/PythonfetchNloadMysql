import pymysql
import sqlalchemy
import os
import pandas as pd

from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class MysqlConn(object):
    def __init__(self):
        self.host=os.getenv("host")
        self.user=os.getenv("user")
        self.password=os.getenv("password")
        self.db=os.getenv("db")

    def pymysql_connect(self):
        return pymysql.connect(host=self.host,
                                user=self.user,
                                password=self.password,
                                db=self.db,
                                cursorclass=pymysql.cursors.DictCursor)

    def pymysql_get_dataframe(self,query="",conn=""):
        return pd.read_sql(sql=query,con=conn)

class SQlAlchemyOperation(object):
    def __init__(self):
        self.host=os.getenv("host")
        self.user=os.getenv("user")
        self.password=os.getenv("password")
        self.db=os.getenv("db")

    def get_sqlalchemy_conn(self,database_name=""):
        return sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(self.user, self.password, 
                                                      self.host, database_name))
    def sqlalchemy_get_dataframe(self,query="",conn=""):
        return pd.read_sql(sql=query,con=conn)

    def append_db(self,df,conn="",tabl_name="",schema="",action="fail",size=1000):    
        #df.to_sql(con=database_connection,name='tmp_tbl_company',schema='tmp',if_exists='append',index=False)
        df.to_sql(con=conn,name=tabl_name,schema=schema,if_exists=action,index=False,chunksize=size,index_label='address_id')
