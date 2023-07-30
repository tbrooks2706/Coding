#https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [5, 10, 15, 20, 25]

def first_and_last(input_list):
    return [input_list[0], input_list[-1]]
print(first_and_last(a))