from datetime import *

birthday = datetime(1994, 2, 15, 4, 25, 12)
print(birthday)
print(birthday.month)
print(datetime.now())
#for iteration in range(0, 10):
#    print(datetime.now())
print(datetime(2022,1,1) - datetime(2021,1,1))

parsed_date = datetime.strptime("Jan 5, 2018", "%b %d, %Y")
print(parsed_date)

date_string = datetime.strftime(datetime.now(), "The year is %Y, month %b, day %d")
print(date_string)
