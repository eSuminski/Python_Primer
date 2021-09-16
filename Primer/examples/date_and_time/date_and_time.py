import datetime

todays_date = datetime.datetime.now()

print(todays_date)
print(todays_date.year)
print(todays_date.month)
print(todays_date.day)
print(todays_date.strftime("%A"))
# there are many different ways to format the time...

my_custom_date = datetime.datetime(2021, 11, 23) # this sets the reference to the given date

print(my_custom_date)