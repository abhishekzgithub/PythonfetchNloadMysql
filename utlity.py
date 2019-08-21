def load_address_lookup_table_df(df,tbl_name="address_input",dbaction="fail"):
    """
    Dump the web address lookup data into the address_input table
    """
    sql_obj.append_db(df,conn=web_address_lookup_table_conn,tabl_name=tbl_name,schema="web_address_lookup",action=dbaction)

def get_address_input_df(queries=constants.q_address_input):
    """
    Get the address input table's data into a dataframe
    """
    address_input_data=pymysql_obj.pymysql_get_dataframe(query=queries,conn=conn)
    return address_input_data

def get_address_output_format():
    df=pd.DataFrame(columns=["address_id", "http_response_code", "redirected_to_url", "html", "lookup_timestamp"])
    df["lookup_timestamp"]=constants.now_time
    return df
