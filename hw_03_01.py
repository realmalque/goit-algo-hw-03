import datetime

def get_days_from_today(date):
    today = datetime.datetime.today()
    hw_deadline = datetime.datetime(year=2024, month=4, day=21, hour=23, minute=45)
    difference = today - hw_deadline
    print (difference.days)
  
