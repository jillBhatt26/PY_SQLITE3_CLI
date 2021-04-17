from config import *
from menu_handler import menu_handler

def add_customer(fName, lName, Email):
    sql = "INSERT INTO customers VALUES(:first_name, :last_name, :email)"
    crs.execute(sql, {'first_name': fName, 'last_name': lName, 'email': Email})
    conn.commit()

    if crs.rowcount == 1:
        print('New customer added!!')
    else:
        print('Failed!')

def display_all_customers():
    sql = "SELECT * FROM customers"
    crs.execute(sql)

    result = crs.fetchall()

    for row in result:
        print(f'\nFirst Name: {row[0]}')
        print(f'Last Name: {row[1]}')
        print(f'Email: {row[2]}\n')

def delete_customer(f_name):
    sql = "DELETE FROM customers WHERE f_name LIKE :fName"
    crs.execute(sql, {'fName': f_name})
    conn.commit()

    if crs.rowcount == 1:
        print(f'Customer: {f_name} deleted successfully!!')
    else:
        print('Deletion failed!!')

def search_customer(f_name):
    search = '%' + f_name + '%'
    sql = "SELECT * FROM customers WHERE f_name LIKE :Search"
    crs.execute(sql, {'Search': search})

    result = crs.fetchall()

    for row in result:
        print(f'\nFirst name: {row[0]}')
        print(f'Last name: {row[1]}')
        print(f'Email: {row[2]}\n')

def get_customer_single(f_name):
    sql = "SELECT * FROM customers WHERE f_name LIKE :First"
    crs.execute(sql, {'First': f_name})

    result = crs.fetchone()

    return result

def update_customer(f_name):
    update_field = input('Enter field to update: ')

    if update_field == 'First Name' or update_field == 'first name':
        new_fName = input('Enter the new first name: ')
        update_fName(f_name, new_fName)

    elif update_field == 'Last Name' or update_field == 'last name':
        new_lName = input('Enter the new last name: ')
        update_lName(f_name, new_lName)

    elif update_field == 'email' or update_field == 'Email':
        new_email = input('Enter the new email: ')
        update_email(f_name, new_email)
    
    else:
        print('Field doesn\'t exist.')
        input('\nPress any key to continue...')
        menu_handler()

def update_fName(old_f_name, new_fName):
    sql = "UPDATE customers SET f_name = ? WHERE f_name = ?"
    crs.execute(sql, (new_fName, old_f_name))
    conn.commit()

    if crs.rowcount == 1:
        print('Updated successfully')
    else:
        print('Updating Failed!!')
    

def update_lName(old_f_name, new_lName):
    sql = "UPDATE customers SET l_name = ? WHERE f_name = ?"
    crs.execute(sql, (new_lName, old_f_name))
    conn.commit()

    if crs.rowcount == 1:
        print('Updated successfully')
    else:
        print('Updating Failed!!')

def update_email(old_f_name, new_Email):
    sql = "UPDATE customers SET email = ? WHERE f_name = ?"
    crs.execute(sql, (new_Email, old_f_name))
    conn.commit()

    if crs.rowcount == 1:
        print('Updated successfully')
    else:
        print('Updating Failed!!')

print(get_customer_single('myname'))