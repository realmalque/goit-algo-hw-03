import datetime

day = datetime.date(2024, 4, 17)
time = datetime.time(16, 37, 52)
full = datetime.datetime.combine(day, time)
print(full)
sd = datetime.datetime(2024, 11, 30, 11, 59, 56, 2)
print(sd)

print(sd.weekday())

day1 = datetime.datetime(2024,11,29,11)

print(sd<=day1)

diff = sd - day1
print(diff)

delay = datetime.timedelta(weeks=3, days=8, hours=3.5)
diff2 = sd + delay
print(diff2)

print(f' ordinal number of {sd} eqauls to {sd.toordinal()}, and another is {diff2.toordinal()}')

sd_stamp = datetime.datetime.timestamp(sd)
print(sd_stamp)

timestamp = 60
obj = datetime.datetime.fromtimestamp(timestamp)
print(obj)

form_day1 = day1.strftime('%Y/%B/%d %H:%m %p %a')
print(form_day1)

from datetime import datetime

# Поточна дата та час
now = datetime.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()


print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

from datetime import datetime, timezone

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(local_now)
print(utc_now)  # Виведе поточний час в UTC

from datetime import datetime, timedelta, timezone

lc_tz = timezone(timedelta(hours=-2))
lc_time = datetime(2024, 5, 25, 15, 45, 0, tzinfo=lc_tz)
utc_time = lc_time.astimezone(timezone.utc)
print(utc_time)

import time

current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

import time

# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів
time.sleep(3)
# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")
