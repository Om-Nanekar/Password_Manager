import random
from datetime import datetime
import json
from tabulate import tabulate

master_password = 'abcd1234'
password_history_list = []

def saveData():
    with open('password_history.json', 'w') as file:
        json.dump(password_history_list, file)

def loadData():
    try:
        with open('password_history.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
            return []
    
password_history_list = loadData()

def create_password():
    lowerLatters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    upperLatters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', '~']


    # 1 symbol, 1 upper, 2 lower, 1 no, 2 symbol, 3 lower, 4 no, 2 upper 

    pos1 = random.choice(symbols)

    pos2 = random.choice(upperLatters)

    pos3 = random.choice(lowerLatters)
    pos4 = random.choice(lowerLatters)

    pos5 = random.choice(numbers)

    pos6 = random.choice(symbols)
    pos7 = random.choice(symbols)

    pos8 = random.choice(lowerLatters)
    pos9 = random.choice(lowerLatters)
    pos10 = random.choice(lowerLatters)

    pos11 = random.choice(numbers)
    pos12 = random.choice(numbers)
    pos13 = random.choice(numbers)
    pos14 = random.choice(numbers)

    pos15 = random.choice(upperLatters)
    pos16 = random.choice(upperLatters)

    password = (f'{pos1}{pos2}{pos3}{pos4}{pos5}{pos6}{pos7}{pos8}{pos9}{pos10}{pos11}{pos12}{pos13}{pos14}{pos15}{pos16}')

    print(f'PASSWORD - \n{password}')


def add_new_pass():
# _Hvw3~,ztl2162PF

    mail = input('Enter your mail - \n')
    url = input('Enter website URL - \n')
    user_name = input('Enter your User name - \n')
    new_password = input('Enter your password -\n')
    now = datetime.now()
    date = now.strftime("%d-%m-%y") 
    time = now.strftime("%H:%M:%S")

    information = f'{mail}, {url}, {user_name}, {new_password}, {date}, {time}'
    password_history_list.append(information)

    saveData()
    print('Password Added !!!!')


def show_past_password():
    data = [item.split(', ') for item in password_history_list]
    headers = ["Mail", "URL's", "User Name", "Password", "Date", "Time"]
    print(tabulate(data, headers=headers, tablefmt='grid'))

def manu():
    user_mater_password = input('Enter password to open - \n')

    if user_mater_password == master_password:
        print('Enter 1 for Creating a Password\n2 for Add new Password\n3 for Show past Passwords\n4 for Exit\n')

        while True:

            user_choice = input('Enter your choice - \n')

            try:
                user_choice = int(user_choice)

                if user_choice == 1 :
                    create_password()

                elif user_choice == 2 :
                    add_new_pass()

                elif user_choice == 3 :
                    show_past_password()
                elif user_choice == 4 :
                    print('Thanks for visiting !!!!!')
                    break
                else:
                    print('Enter valid input !!\n')

            except ValueError :
                print('Enter valid input')


    else:
        print('Invalid Password !!!!')

manu()