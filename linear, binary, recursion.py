import math
import random

def find_factorial_iter(num):
    if type(num) is not int or num < 1:
        return "Input a positive integer."
    num_a = num
    fact = num
    for x in range(num):
        if num_a == 1:
            break
        num_a -= 1
        fact *= num_a 
    return fact

#print(find_factorial_iter(11))

def find_factorial_rec(num):
    if num == 1:
        return 1
    else:
        return num * find_factorial_rec(num - 1)

# factorial(n) = n × factorial(n – 1)

print(find_factorial_rec(5))

def countdown(n):
    print(n)
    #exit condition
    if n == 0:
        #this is the point at which you stop recurring - exit condition
        return             # Terminate recursion
    #recursion
    else:
        #this is the thing you keep doing till you get to exit condition
        countdown(n - 1)   # Recursive call

#countdown(5)

data = [random.randint(1, 50000) for x in range(1, 500)]
#print(data)

#return index number of data in an array
def linear_search(data, target):
    ind = 0
    for item in data:
        if item == target:
            return ind
        ind += 1
    return None

print("Linear",linear_search(data, 500))

#return index number of data in an array
def binary_search(data, target):
    sorted_list = sorted(data)
    min = 0
    max = len(sorted_list) - 1
    ind = 0
    stop = False
    while stop == False:
        mid = min + math.floor((max - min) / 2)
        guess = sorted_list[mid]
        if guess == target:
            ind = mid
            stop = True
        elif mid == max:
            ind = None
            stop = True
        elif guess > target:
            max = mid - 1
        else:
            min = mid + 1
    return ind

print("Binary",binary_search(data, 500))