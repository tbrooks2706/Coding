#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

input_num = int(input("Enter a number: "))
div_num = int(input("Enter a divisor: "))
print("Does divisor divide into number?")
if input_num % div_num == 0:
    print("Yes!")
elif div_num % 4 == 0:
    print("No, but multiple of 4")
elif div_num % 2 == 0:
    print("No, but even")
else:
    print("No, but odd")