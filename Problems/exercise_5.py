#https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set([x for x in a if x in b]))

c = random.sample(range(100), k=15) #k is number of values, sequence is the list to randomly select elements from
d = random.sample(range(100), k=15)
print(set([x for x in c if x in d]))
