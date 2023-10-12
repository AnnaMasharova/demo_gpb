from postgre_connection import take_cursor, cursor_close
from feature_toggle import feature_toggle_dict
from psycopg2 import Error
from sql_querry import *
import json


def idf_method_account (data_json):
    
    
    method = data_json['method']
    
    
    if method == 'create' and feature_toggle_dict['account_create']==1:
       return mtd_create_account (data_json)
    elif method == 'get':
         return mtd_get_account(data_json)
    elif method == 'delete':
         return mtd_delete_account(data_json)
    elif method == 'update':
         return mtd_update_account(data_json)
    else:
        return mtd_not_allow()  


def mtd_create_account (data_json, ):
       
    connect_result = take_cursor()

    cursor = connect_result[0]
    connection = connect_result [1]    
    
    account_id = data_json['data']['account_id']
    balance = data_json['balance']
       
    
    
    try:
        cursor.execute(create_account, (account_id, balance, ))
        connection.commit()       
        
        
        response  = {
            "result": "ok",
            "reason": "new_account_is_created"
        }

        
    except(Exception, Error) as error:
        response  = {
            "result": "fail",
            "reason": error
        }
        
    json_response = json.dumps(response)
    
    cursor_close(cursor, connection)    
    return json_response
    
    
def mtd_get_account (data_json):
      
    connect_result = take_cursor()

    cursor = connect_result[0]
    connection = connect_result [1]    
    
    try:
        account_id = data_json['data']['account_id']
        
       
        cursor.execute(get_user, (account_id, ))
        rows = cursor.fetchmany(1)
        
        print (rows)
        
        balance = rows[0][0]
        account_id_res = rows[0][1]
        
        response  = {
        "result": "ok",
        "data":{
            "balance": balance,
            "account_id": account_id_res
                }
        }
    
    except(Exception, Error) as error:
        print (error)
        
        response  = {
            "result": "fail",
            "reason": error
        }
    
    
    json_response = json.dumps(response)
    
    cursor_close(cursor, connection)    
    return json_response
    
    
def mtd_update_account (data_json):
      
    connect_result = take_cursor()

    cursor = connect_result[0]
    connection = connect_result [1]    
    
    try:
        
        account_id = data_json['data']['account_id']
        balance = data_json['balance']

      
       
        cursor.execute(update_account, (balance, account_id, ))
        connection.commit()
        count_row = cursor.rowcount
        
        
        
        if count_row != 0:
            account_id_res = '{0} is updated'.format(account_id)
        else:
            account_id_res = '{0} is not exist'.format(account_id)
        
        response  = {
        "result": "ok",
        "data":{
            "account_id": account_id_res
                }
        }
    
    except(Exception, Error) as error:
        print (error)
        
        response  = {
            "result": "fail",
            "reason": error
        }
        
    json_response = json.dumps(response)
    
    cursor_close(cursor, connection)    
    return json_response   
    
        
def mtd_not_allow ():  
    response  = {
        "result": "ok",
        "reason": "method not allow"
    }
    
    json_response = json.dumps(response)
    return json_response
    


def mtd_delete_account (data_json):
      
    connect_result = take_cursor()

    cursor = connect_result[0]
    connection = connect_result [1]    
    
    try:
        
        account_id = data_json['data']['account_id']
        
       
        cursor.execute(delete_account, (account_id, ))
        count_row = cursor.rowcount
        connection.commit()
        
        
        
        
        if count_row != 0:
            account_id_res = '{0} is deleted'.format(account_id)
        else:
            account_id_res = '{0} is not exist'.format(account_id)
        
        response  = {
        "result": "ok",
        "data":{
            "account_id": account_id_res
                }
        }
    
    except(Exception, Error) as error:
        print (error)
        
        response  = {
            "result": "fail",
            "reason": error
        }
        
    json_response = json.dumps(response)
    
    cursor_close(cursor, connection)    
    return json_response
    