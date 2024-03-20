import math

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
    def do_recursion(running_total, multiplier):
        if multiplier == 1:
            return running_total
        else:
            do_recursion(running_total * multiplier, multiplier - 1)
    
    return do_recursion(num, num - 1)

#print(find_factorial_rec(5))

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

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#return index number of data in an array
def linear_search(data, target):
    ind = 0
    for item in data:
        if item == target:
            return ind
        ind += 1
    return None

#print(linear_search(primes, 97))

#return index number of data in an array
def binary_search(data, target):
    sorted_list = sorted(data)
    min = 0
    max = len(sorted_list) - 1
    ind = 0
    stop = False
    while stop == False:
        mid = min + math.floor((max - min) / 2)
        guess = data[mid]
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

print(binary_search(primes, 17))