#https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

def is_prime(num):
    to_check = range(1, num)
    divisors = [1, num]
    for a in to_check:
        if a not in divisors and num % a == 0:
            divisors.append(a)
    if len(divisors) == 2:
        return True
    return False

number = int(input("Enter a number: "))
print("Prime:", is_prime(number))
             