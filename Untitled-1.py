from datetime import datetime
def now():
    for iteration in range (0, 10):
        print(datetime.now())

def greeting(name):
    print("Hello, "+name+"!") 

greeting("Tom")
now()