# import datetime

# def get_days_from_today(date):
#     today = datetime.datetime.today()
#     hw_deadline = datetime.datetime(year=2024, month=4, day=21, hour=23, minute=45)
#     difference = today - hw_deadline
#     print (difference.days)


# from datetime import datetime
# # Встановлення дати 
# hw_deadline = datetime(year=2024, month=4, day=21)
# # Поточна дата
# current_date = datetime.now()
# # Розрахунок кількості днів
# days_since = hw_deadline.toordinal() - current_date.toordinal()
# print(days_since)