import os
from database import *
import setup

def menu_handler():
    os.system('cls')

    print('***Customer Management System***')
    print('1. Enter new customer.')
    print('2. Display all customers.')
    print('3. Update a customer.')
    print('4. Delete a customer.')
    print('5. Search a customer.')
    print('6. Exit application.')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        os.system('cls')
        f_name = input('Customer\'s first name: ')
        l_name = input('Customer\'s last name: ')
        email = input('Customer\'s email: ')
        add_customer(f_name, l_name, email)
        input('Press any key to continue...')
        menu_handler()

    elif choice == 2:
        os.system('cls')
        print('All customers => ')
        display_all_customers()
        input('Press any key to continue...')
        menu_handler()

    elif choice == 3:
        os.system('cls')
        f_name = input('Customer\'s first name: ')
        customer = get_customer_single(f_name)

        if customer == None:
            print('Customer not found!!')
            input('Press any key to continue...')
            menu_handler()

        else:
            update_customer(f_name)
            print(f'{f_name} updated.')
            input('Press any key to continue...')
            menu_handler()

    elif choice == 4:
        os.system('cls')
        f_name = input('Customer\'s first name: ')
        delete_customer(f_name)
        input('Press any key to continue...')
        menu_handler()

    elif choice == 5:
        os.system('cls')
        f_name = input('Customer\'s first name: ')
        print(f'{f_name} info.')
        search_customer(f_name)
        input('Press any key to continue...')
        menu_handler()

    elif choice == 6:
        exit()

    else:
        os.system('cls')
        print('Enter valid choice.')
        input('Press any key to continue...')
        menu_handler()

if __name__ == '__main__':
    menu_handler()