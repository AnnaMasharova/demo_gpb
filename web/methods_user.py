from postgre_connection import take_cursor, cursor_close
from feature_toggle import feature_toggle_dict
from psycopg2 import Error
from sql_querry import *
import json


def idf_method (data_json):
    
    
    method = data_json['method']
    
    
    if method == 'create' and feature_toggle_dict['user_create']==1: 
       return mtd_create_user(data_json)
    elif method == 'get':
         return mtd_get_user(data_json)
    elif method == 'delete':
         return mtd_delete_user(data_json)
    elif method == 'update':
         return mtd_update_user(data_json)
    else:
        return mtd_not_allow()     

def mtd_create_user (data_json):
    
    
    connect_result = take_cursor()

    cursor = connect_result[0]
    connection = connect_result [1]    
    
    name = data_json['data']['name']
    email = data_json['data']['email']
    password = data_json['data']['password']
       
    
    
    try:
        cursor.execute(create_user, (name, email, password, ))
        connection.commit()
               
        
    
        cursor.execute("select account_id from accounts.user_table order by id desc", "\n")
        new_account_id = cursor.fetchmany(1)


        new_account_id_res = 'user is created: {}'.format (new_account_id[0][0])
        
        
        
        response  = {
            "result": "ok",
            "reason": new_account_id_res
        }

        
    except(Exception, Error) as error:
        response  = {
            "result": "fail",
            "reason": error
        }
        
    json_response = json.dumps(response)
    
    cursor_close(cursor, connection)    
    return json_response
    
    
    
    
    
   
def mtd_delete_user (data_json):
      
    connect_result = take_cursor()

    cursor = connect_result[0]
    connection = connect_result [1]    
    
    try:
        
        account_id = data_json['data']['account_id']
        
       
        cursor.execute(delete_user, (account_id, ))
        connection.commit()
        count_row = cursor.rowcount
        
        
        
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
    
def mtd_update_user (data_json):
      
    connect_result = take_cursor()

    cursor = connect_result[0]
    connection = connect_result [1]    
    
    try:
        
        account_id = data_json['data']['account_id']
        name = data_json['data']['name']
        email = data_json['data']['email']
        password = data_json['data']['password']
      
       
        cursor.execute(update_user, (name, email, password, account_id, ))
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
    
def mtd_get_user (data_json):
      
    connect_result = take_cursor()

    cursor = connect_result[0]
    connection = connect_result [1]    
    
    try:
        account_id = data_json['data']['account_id']
        
       
        cursor.execute(get_user, (account_id, ))
        rows = cursor.fetchmany(1)
        
        
        if len(rows) == 0:
            
            account_id_res = '{0} is not exist'.format(account_id)
            
            response  = {
                "result": "ok",
                "reason": account_id_res
            }
            
        else:
            
            print (rows)
            
            user_name = rows[0][0]
            email = rows[0][1]
            password = rows[0][2]
            account_id_res = rows[0][3]
            
            
            
            response  = {
            "result": "ok",
            "data":{
                "name": user_name,
                "email": email,
                "password": password,
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
    