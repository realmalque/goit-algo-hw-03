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
print(cats_info)