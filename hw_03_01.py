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
