import general_functions
import copy
init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_6.txt")
test_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_6_test.txt")
#print(test_list)

def format_list(raw_list):
    new_list = raw_list[0].split(",")
    for index in range(len(new_list)):
        new_list[index] = int(new_list[index])
    return new_list

working_list = format_list(init_list)
#print(working_list)

class Fish:
    lifespan = 8
    def __init__(self, timer) -> None:
        self.timer = timer
        self.created_today = False

class NewFish(Fish):
    def __init__(self):
        super().__init__(self.lifespan)
        self.created_today = True

#Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.
#how many lanternfish after 18 days(test only)? after 80 days?

def pass_day(input_list):
    created_fish = []
    new_list = []
    for index in range(len(input_list)):
        num = input_list[index]
        this_fish = Fish(num)
        if this_fish.timer == 0:
            created_fish.append(8)
            new_list.append(6)
        else:
            new_list.append(this_fish.timer - 1)
    end_list = new_list + created_fish
    return end_list

def pass_days(input_list, number_of_days):
    new_list = copy.deepcopy(input_list)
    for num in range(number_of_days):
        updated_list = pass_day(new_list)
        new_list = updated_list
    return new_list

#print(pass_days(working_list, 4))

#answer part 1
list_part_1 = pass_days(working_list, 80)
fish_1 = len(list_part_1)
print(fish_1)

#answer part 2
list_part_2 = pass_days(working_list, 256)
fish_2 = len(list_part_2)
print(fish_2)