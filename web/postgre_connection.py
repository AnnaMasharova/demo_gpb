import psycopg2
from psycopg2 import Error



def take_cursor ():
    
    password = 'gpbuworker'
    user = 'gpbuworker'
    port = '5432'
    host = 'postgres'
    database = 'accounts'
    
    try:
        connection = psycopg2.connect(
            
            user = user,
            password = password, 
            host = host,
            port = port,
            database = database
            
        )
        cursor = connection.cursor()

        print (cursor)
        
        print ('Подключились к postgre')
        return cursor, connection
    
    except (Exception, Error) as error:
        print ("Ошибка при работе Postgre", error)
        
        
        
def cursor_close (cursor, connection):
    try:
        cursor.close()
        connection.close()
        print ('Соединение postgre закрыто')
    except (Exception, Error) as error:
        print("Ошибка Postgre" , error)
        
    print (cursor)