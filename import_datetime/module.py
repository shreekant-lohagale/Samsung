import datetime
print(datetime.datetime.now())


today = datetime.date.today()
print("Today's date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

start_time = datetime.datetime.now()
start_time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")
print("Start Time:", start_time_str)

import datetime as dt
start_time = dt.datetime.now()
start_time.replace(month = 12, day = 25)