# import datetime

# day = datetime.date(2024, 4, 17)
# time = datetime.time(16, 37, 52)
# full = datetime.datetime.combine(day, time)
# print(full)
# sd = datetime.datetime(2024, 11, 30, 11, 59, 56, 2)
# print(sd)

# print(sd.weekday())

# day1 = datetime.datetime(2024,11,29,11)

# print(sd<=day1)

# diff = sd - day1
# print(diff)

# delay = datetime.timedelta(weeks=3, days=8, hours=3.5)
# diff2 = sd + delay
# print(diff2)

# print(f' ordinal number of {sd} eqauls to {sd.toordinal()}, and another is {diff2.toordinal()}')

# sd_stamp = datetime.datetime.timestamp(sd)
# print(sd_stamp)

# timestamp = 60
# obj = datetime.datetime.fromtimestamp(timestamp)
# print(obj)

# form_day1 = day1.strftime('%Y/%B/%d %H:%m %p %a')
# print(form_day1)

# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)
# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()


# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC

# from datetime import datetime, timedelta, timezone

# lc_tz = timezone(timedelta(hours=-2))
# lc_time = datetime(2024, 5, 25, 15, 45, 0, tzinfo=lc_tz)
# utc_time = lc_time.astimezone(timezone.utc)
# print(utc_time)

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")

# import time

# # Записуємо час на початку виконання
# start_time = time.perf_counter()

# # Виконуємо якусь операцію
# for _ in range(1_000_000):
#     pass  # Просто проходить цикл мільйон разів
# # time.sleep(3)
# # Записуємо час після виконання операції
# end_time = time.perf_counter()

# # Розраховуємо та виводимо час виконання
# execution_time = end_time - start_time
# print(f"Час виконання: {execution_time} секунд")


# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# #print(query)

# s = 'hello this is me you\'re looking for'
# _, sec_half = s.split('this')
# dic = {}
# for el in sec_half.split(' '):
#     key, value = el.split('e')
# print(sec_half)

# song = ['hello', 'this', 'is', 'me', 'is', "you're", 'is', 'looking', 'for']
# result = ' '.join(song) 
# print(result.replace('is',' '))

# check = 'lkjhg 23 dewkf'
# for i in check:
#     if i.isdigit():
#         print( f'{i} is a real number', end = ' ')
#     else:
#         print (f'{i} is a bullshit')

# intrans = '_)(*?:%:?*())(*?:;)'
# transtr = str.maketrans('','', intrans)
# str = 'Haku:?*(na ;%:?*(matat?*()a ?*(Oh-oh-oh I _)(*?:see u'
# print(str.translate(transtr))

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# print(MAP)

# result = "34 DF 56 AC".translate(MAP)
# print(result)

# import random 
# rand_num = random.randint(1, 5)
# user_num = int(input("Guess the num 1-5?: "))

# if user_num == rand_num:
#     print("Hell yeah!")
# else:
#     print('no way bust!')
#     print(f'corect was {rand_num}, you asshole')

# from colorama import init
# found = None
# for i in "hello world":
#     if i == 'h':
#         found = True
#         break
#     else:
#         found = False
    
# print(found)

# lis =  [3, 4, 'stroka', True, 14.6]
# print(lis[::-2])

# name = "Dima"
# age = 35

# message = 'Test 2. My name is {}, my age is {} years'.format(name, age)
# print(message)

# mes = 'Test 3. My name is %s. I am %d years old' % (name, age)
# print(mes)

# mas = 'Test 4. My name is ' + name + 'I am ' + str(age) + ' years old'
# print(mas)

# round(age)

# el_1 = 'Hello ' + 'world'
# el_2 = 'Hello world'
# print(f'eqaul {el_1 == el_2}')
# print(f'ident {el_1 is el_2}')
# print(id(el_1))
# print(id(el_2))

# floors = 5
# app_per_floor = 4 

# app_num = int(input('Enter the appartment number: '))
# app_per_entarnce = app_per_floor * floors
# entrancen_num = (app_num -1) // app_per_entarnce + 1
# floor_num = ((app_num - 1) % app_per_entarnce) // app_per_floor + 1 
# print (f'Entrance nu\'mber is {entrancen_num} and floor numbefr is {floor_num}')

# try:
#     with open('text.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
    
# except FileNotFoundError:
#     print ("File was not found")

# from math import sqrt as s, floor
# print(floor(s(100)))

# class Building:
#     year = None
#     city = None

#     def __init__(self, year, city):
#         self.year = year
#         self.city = city

#     def get_info(self):
#         print('Year: ', self.year, 'City: ', self.city)

# class School(Building):
#     pupils = 0

#     def __init__(self, pupils, year, city):
#         super(School, self).__init__(year,city)
#         self.pupils = pupils

#     def get_info(self):
#         super().get_info()
#         print('Pupils: ', self.pupils)

# class Shop(Building):
#     pass

# class Museum(Building):
#     pass

# school = School(100, 2015, 'Kyiv')
# school.year = 5 
# school.get_info()
# shop = Shop(2015, 'Kyiv')
# museum = Museum(2015, 'Kyiv')
# museum.get_info()

# import webbrowser

# def validator(func):
#     def wrapper(url):
#         if "." in url:
#             func(url)
#         else:
#             print('Wrong url')
#     return wrapper

# @validator
# def open_url(url):
#     webbrowser.open(url)

# open_url('https://google.com')

# countries = ('Denmark', 'USA', 'Sweeden', 'Canada')
# (blue, green, yellow, white) = countries
# print(yellow)

# new_list = [x for x in countries if x != "USA"]
# countries.sort(key= str.lower)
# # for x in countries:
# #     if 'a' in x.lower():
# #         new_list.append(x)
# sec_new_list =  ['Opa' for x in countries]
# third_list = [y if y == 'Denmark' else 'Lol' for y in countries]
# print(new_list, sec_new_list, third_list)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)

# print(countries)

# from datetime import datetime
# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "Sarah Lee", "birthday": "1957.3.23"},
#     {"name": "Jonny Lee", "birthday": "1958.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]
# for x in users:
#     date_string = x['birthday']
# print(date_string)
# def string_to_date(date_string):
#     converted_date = string_to_date(date_string)
#     timedelta = converted_date - datetime.today
#     print(timedelta)


# from datetime import datetime
# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]
# def string_to_date(users['birthday']):
#     return datetime.strptime(users['birthday'], "%Y.%m.%d").date()

my_list = [1, 2, 3, 5, None, 7, 346, 235, 235, None, 347, -435, None, -23, 0]
# print(my_list)

# print(my_list.index(None))

while my_list:
    if None not in my_list:
        break
    my_list.pop(my_list.index(None))

# while True:
#     if None not in my_list:
#         break
#     my_list.pop(my_list.index(None))

# print(my_list)

# value_x, value_y = 5, 5

# # if value_x > value_y:
# #     print(value_x)
# # else:
# #     print(value_y)

# # max_value = value_x if value_x > value_y else value_y
# # print(max_value)

# # max_value = 'X > Y' if value_x > value_y else "X < Y"
# # print(max_value)

# max_value = 'X > Y' if value_x > value_y else "X < Y" if value_x < value_y else "X = Y"
# print(max_value)

# max_value = 'X = 0 or Y = 0' if value_x == 0 or value_y == 0 else "X != 0 and Y != 0"
# # print(max_value)
# def say(message, times=1):
#     print(message * times)

# say('Привіт') 
# say('Світ', 5)

# my_list = [1, 2, 3]
# a, *rest = my_list
# print(a, rest)

# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)

# def fibonachi(number):
#     return number if number == 0 or number == 1 else fibonachi(number-2) + fibonachi(number-1)

# print(fibonachi(10))

# print(pow(2,3))

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else: 
#         return base * power(base, exponent-1)
    
# print(power(2,3))
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num >= 0:
#     sum += num
#     num -=1
    
# print(sum)

# from datetime import datetime

# date = datetime(year = 2002, month = 9, day = 11)
# ordinal = date.toordinal()
# times = datetime.timestamp(date)
# dt_obj = datetime.fromtimestamp(times)
# print(ordinal, times, dt_obj , sep="\n")

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)

# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)

# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC

# from datetime import datetime, timezone, timedelta

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)  
# local_time = datetime.now()
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC
# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")



# name = "Alice"
# formatted = f"{name:^10}"
# print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)


# import re

# text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)

# if match:
#     print("Знайдено:", match.string)
# else:
#     print("Не знайдено.")

# import re

# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())
# from datetime import datetime, date, timedelta

# from datetime import datetime, date, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")


# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list


# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)
# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         return find_next_weekday(birthday, 0)
#     return birthday
# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         """
#         Додайте на цьому місці перевірку, чи не буде 
#         припадати день народження вже наступного року.
#         """
#         if (birthday_this_year - today).days <= 0:
#             return birthday_this_year + timedelta(days=abs(birthday_this_year - today))
#         if 0 <= (birthday_this_year - today).days <= days:
#             return find_next_weekday(birthday_this_year,0)
#             """
#             Додайте перенесення дати привітання на наступний робочий день,
#             якщо день народження припадає на вихідний. 
#             """
#             congratulation_date_str = date_to_string(birthday_this_year)
#             upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
#     return upcoming_birthdays




# import re

# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	

# import re

# txt = "mn"


# x = re.findall("ma*n", txt)

# print(x)

# elements = ['earth', 'air', 'fire', 'water']
# result = ', '.join(elements)
# print(result.title())  # Виведе: 'earth, air, fire, water'

# for i in range(8):
#     s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
#     print(s)

# width = 5
# for num in range(12):
#     print(f'|{num:^10} | {num**2:^10} | {num**3:^10}|')
import re

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)

import re

text = "Python - це проста, але потужна мова програмування."
pattern = r"\w+"
matches = re.findall(pattern, text)

print(matches)  # Виведе список всіх слів у рядку

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)

