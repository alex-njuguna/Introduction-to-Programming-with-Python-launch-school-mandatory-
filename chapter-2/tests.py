from datetime import datetime as dt

date = dt.strptime("14 August 1995", "%d %B %Y")
weekday_name = date.strftime('%A')
print(weekday_name)                   # Saturday


date_string = "October 16, 2022"
date_format = "%B %d, %Y"

# Convert the string to a datetime object
date_object = dt.strptime(date_string, date_format)
print(date_object)

full_weekday_name = date_object.strftime('%A')
print(full_weekday_name)