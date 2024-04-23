#_____________________________________Задача_01_04_____________________________________
from pathlib import Path


def total_salary(path):

    with open('salary_list.txt', 'r') as file:
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
    with open('Cats_info.txt', 'r') as file:
        try:
            cats_info = list()
            for line in file:
                every_cat = {'id':line.split(',')[0],'name':line.split(',')[1],'age':line.split(',')[2].strip()}    
                cats_info.append(every_cat)
            return cats_info
         
        except OSError:
            print('Error while reading file')

cats_info = get_cats_info('Cats_info.txt')
print(cats_info)