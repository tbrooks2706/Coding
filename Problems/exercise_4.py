#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

num_1 = int(input("Enter a number: "))
div = [x for x in range(1, num_1 + 1) if num_1 % x == 0]
print(div)