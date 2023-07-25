#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input("Enter name: ") #enter "Tom"
#print("Hello",name) #prints "Hello Tom"
age = input("Enter age: ")
times_to_print = int(input("Times to print message: "))
year_100 = 2023 + (100 - int(age))
print(name, age) #prints "Tom 35"
for x in range(times_to_print):
    print("You will be 100 in", year_100)
