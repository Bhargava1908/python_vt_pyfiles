# Datetime Module
from datetime import date, time, datetime, timedelta


today_date = date.today()
print(type(today_date))
print(today_date)

current_timestamp = datetime.now()
print(type(current_timestamp))
print(current_timestamp)

my_format1 = "%y/%m/%d %H:%M:%S"
current_timestamp_str = current_timestamp.strftime(my_format1)
print(type(current_timestamp_str))
print(current_timestamp_str)


random_timestamp_str = "2025-10-16 09:17:00"
print(type(random_timestamp_str))
my_format2 = "%Y-%m-%d %H:%M:%S"
random_timestamp_datetime = datetime.strptime(random_timestamp_str, my_format2)
print(type(random_timestamp_datetime))
print(random_timestamp_datetime)

current_timestamp = datetime.now()
after_30_days_from_now = current_timestamp + timedelta(days=30)
print(after_30_days_from_now)

dec_21_date_str = "21-12-2025 12:00:00"
my_format3 = "%d-%m-%Y %H:%M:%S"
dec_21_date = datetime.strptime(dec_21_date_str, my_format3)
days_30_after_dec_21 = dec_21_date + timedelta(days=30)
print(days_30_after_dec_21)


current_timestamp = datetime.now()
two_weeks_from_now = current_timestamp + timedelta(weeks=2)
print(two_weeks_from_now)

current_timestamp = datetime.now()
fifteen_days_from_now = current_timestamp + timedelta(weeks=2, days=1, hours=4, minutes=30)
print(fifteen_days_from_now)


date1_str = "31-10-2025 22:00:00"
date2_str = "01-10-2025 12:00:00"
my_format4 = "%d-%m-%Y %H:%M:%S"
date1_datetime = datetime.strptime(date1_str, my_format4)
date2_datetime = datetime.strptime(date2_str, my_format4)
difference_date1_date2 = date1_datetime - date2_datetime
print(difference_date1_date2)

date1 = date(2025, 10, 31)
print(date1)

datetime1 = datetime(2025, 10, 16, 9, 35, 00)
print(datetime1)

print(datetime.time)

current_timestamp = datetime.now()
print(current_timestamp.year)
print(current_timestamp.month)
print(current_timestamp.day)
print(current_timestamp.hour)
print(current_timestamp.minute)
print(current_timestamp.second)
print(current_timestamp.microsecond)

current_timestamp = datetime.now()
print(current_timestamp.strftime("%a %A %b %B %d-%m-%Y %H:%M:%S"))
print(current_timestamp.strftime("%a %A %b %B %w"))

datetime1 = datetime.fromtimestamp(1887639468)
print(datetime1)

date1 = datetime1.date()
print(type(date1))
print(date1)
date1_str = date1.isoformat()
print(type(date1_str))
print(date1_str)
weekday = date1.isoweekday()
print(weekday)


my_time = time(13, 24, 56)
print("Entered time:", my_time)

my_time = time(minute=12)
print("Time with one argument:", my_time)

my_time = time()
print("Time without argument:", my_time)

Time = time(11, 34, 56)
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

a = datetime(1999, 12, 12, 12, 12, 12)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())


now = datetime.now()
string = datetime.isoformat(now)
print(string)
print(type(string))
