import datetime
import time

# Current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)

# Current date
today = datetime.date.today()
print("Today's Date:", today)

# Current time
current_time = datetime.datetime.now().time()
#datetime module.datetime class. now is a
#  function which returns object which contains 
#year , month, day,hour, min,second,microsecod
# here time will extract only time part of it
print("Current Time:", current_time)

# Get individual components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Formatting datetime
print("Formatted Date (dd-mm-yyyy):", now.strftime("%d-%m-%Y"))
print("Formatted Time (HH:MM:SS):", now.strftime("%H:%M:%S"))

# Creating a custom date
custom_date = datetime.date(2025, 12, 31)
print("Custom Date:", custom_date)

# Date difference
future_date = datetime.date(2025, 12, 31)
delta = future_date - today
print("Days until New Year 2025:", delta.days)

# Adding days to a date
after_10_days = today + datetime.timedelta(days=10)
print("Date after 10 days:", after_10_days)

# Subtracting days from a date
before_10_days = today - datetime.timedelta(days=10)
print("Date before 10 days:", before_10_days)

# Sleep function from time module
print("Waiting for 2 seconds...")
time.sleep(2)
print("Resumed after 2 seconds")
