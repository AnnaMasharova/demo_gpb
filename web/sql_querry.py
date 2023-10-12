create_user = (
    'insert into accounts.user_table '
    '(user_name, email, user_password, account_id, date_add)'
    'values '
    '( %s ,  %s  , %s,  (select gen_random_uuid()), now())'
    )

delete_user = (
'    delete from accounts.user_table where account_id =%s'
)

update_user = (
'   update accounts.user_table '
'   set user_name = %s, email = %s, user_password= %s '
'   where account_id = %s '    
)

get_user = (
    'select * from accounts.user_table where account_id = %s ' 
)







create_account= (
    'insert into accounts.account '
    '(account_id, balanse_value, date_update ) '
    'values '
    '( %s ,  %s, now()) '
        
)   

get_account = (
    'select balanse_value, account_id from accounts.account where account_id = %s ' 
)


update_account = (
'   update accounts.account '
'   set balance = %s '
'   where account_id = %s '    
)


delete_account = (
'    delete from accounts.account where account_id =%s'
)