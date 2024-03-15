from datetime import datetime

def get_days_from_today(date):
    try:
        hw_deadline = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        delta = today - hw_deadline
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

print(get_days_from_today("2024-04-21"))