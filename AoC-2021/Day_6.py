import general_functions
import copy
import datetime
import numpy as np

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_6.txt")
test_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_6_test.txt")
#print(test_list)

def format_list(raw_list):
    new_list = raw_list[0].split(",")
    for index in range(len(new_list)):
        new_list[index] = int(new_list[index])
    new_array = np.array(new_list)
    return new_array

working_list = format_list(test_list)
#print(working_list)

class Fish:
    lifespan = 8
    def __init__(self, timer) -> None:
        self.timer = timer
        self.created_today = False

#Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.
#how many lanternfish after 18 days(test only)? after 80 days?

def pass_day(input_list=np.array([])):
    created_fish = np.array([])
    new_list = np.array([])
    #print(input_list.size)
    for index in range(input_list.size):
        num = input_list[index]
        #print(num)
        this_fish = Fish(num)
        #print(this_fish.timer)
        if this_fish.timer == 0:
            created_fish = np.append(created_fish, 8)
            new_list = np.append(new_list, 6)
        else:
            new_list = np.append(new_list, this_fish.timer - 1)
    end_list = np.append(new_list, created_fish)
    return end_list

#print(pass_day(working_list))

def pass_days(input_list, number_of_days):
    start = datetime.datetime.now()
    new_list = copy.deepcopy(input_list)
    for num in range(number_of_days):
        #print(new_list)
        updated_list = pass_day(new_list)
        new_list = updated_list
    end = datetime.datetime.now()
    print(end - start)
    return new_list

#print(pass_days(working_list, 3))

#answer part 1
list_part_1 = pass_days(working_list, 80)
fish_1 = len(list_part_1)
print(fish_1)

#list_85 = pass_days(working_list, 85)
#list_alt_100 = pass_days(list_85, 65)
#print(len(list_alt_100))
#list_100 = pass_days(working_list, 150)
#print(len(list_100))


#answer part 2
#150 = 2.6m, 9.2s
#170 = 15m, 50.2s
#180 = 35m, 2m18s
list_part_2 = pass_days(working_list, 100)
fish_2 = len(list_part_2)
print(fish_2)
