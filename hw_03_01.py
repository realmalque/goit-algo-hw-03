#_____________________________ЗАДАЧА 1 ______________________________________
from datetime import datetime # імпортуємо модуль та метод

def get_days_from_today(date): # визначаємо функцію
    try:
        hw_deadline = datetime.strptime(date, '%Y-%m-%d') # перетворюємо параметр функції в об'єкт datetime
        today = datetime.today() # отримуємо сьогоднійшню дату
        delta = today - hw_deadline # рахуємо різницю дат 
        return delta.days # повертаємо різницю дат кратну дням
    except ValueError: 
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'." #прописуємо повідомлення в разі неправильної подачі формату дати

print(get_days_from_today("2024-04-21"))

#_____________________________ЗАДАЧА 2 ______________________________________

import random
def get_number_ticket(min, max, quantity):
    winner_set = set() # створюємо пусту множину для наповнення унікальнми вигришеими числами
    while len(winner_set) < quantity: # створюємо цикл що обмежує к-ть виграшних чисел параметром функції
        i = random.randint(min, max) # рандомно обираємо змінні 
        winner_set.add(i) # наповнюємо множину
    winner_list=list(winner_set) # перетворюємл множину на список для подальшого сортування
    winner_list.sort() # сортуємо список
    return winner_list

print(get_number_ticket(1, 1000, 5))

#_____________________________ЗАДАЧА 3 ______________________________________

import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Перевіряємо, чи номер починається з '+'
    if cleaned_number.startswith('+'):
        # Якщо так, то нічого не змінюємо
        return cleaned_number
    else:
        # Якщо ні, додаємо міжнародний код для України '+38'
        return '+38' + cleaned_number[2:] if cleaned_number.startswith('380') else '+38' + cleaned_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
