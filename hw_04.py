#_____________________________________Задача_01_04_____________________________________
from pathlib import Path


def total_salary(path):
    path = Path(path)
    with open('salary_list.txt', 'r', encoding='utf-8') as file:
        try:
            salary = list()
            for line in file:
                salary.append(line.split(',')[1])
            total=0
            for i in salary:
                total += int(i) 
            average = (total / len(salary))
            return total, average
        except OSError:
            print('Error while reading file')

total, average = total_salary('salary_list.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

#_________________________________Задача_02_04________________________________________

from pathlib import Path

def get_cats_info(path):
    path = Path(path)
    with open('Cats_info.txt', 'r', encoding='utf-8') as file:
        try:
            cats_info = []
            for line in file:
                id,name,age = line.strip().split(',')
                cat_dict = {'id':id, 'name':name, 'age':age}
                cats_info.append(cat_dict)
            return cats_info
         
        except OSError:
            print('Error while reading file')

cats_info = get_cats_info('Cats_info.txt')
print(*cats_info, sep='\n')


#_________________________________Задача_03_04________________________________________
# import sys, colorama, pathlib
#_________________________________Задача_04_04________________________________________

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "This contact doesn't exist"
    else:
        del contacts[name]
        contacts[name] = phone
        return "Contact updated"
        
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "This contact doesn't exist"
    
def show_all(contacts):
    return contacts
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
        
if __name__ == "__main__":
    main()

