
import datetime
tday = datetime.date.today()
deadline = datetime.date(2024, 4, 21)
till_dl = deadline - tday
print(till_dl.days)