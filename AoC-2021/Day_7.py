import general_functions
import datetime

init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_7.txt")
test_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_7_test.txt")

def format_list(input_list):
    return [int(x.strip()) for x in input_list[0].split(",")]

working_list = format_list(test_list)
#print(working_list)

#numbers are horizontal position of each crab
#they can only move horizontally
#you have to align them all on one number
#each movement by one crab by one position, costs one fuel (for a crab to move from 16 to 3 costs 13)
#how much fuel will they spend, aligning to the position that costs the least fuel possible?

#find range between largest and smallest number in list
#check every position number in that range
#for each position:
    #run through all crabs, and keep a running total of how much fuel it would cost them all to get there
    #add range number:total fuel to a dictionary

class Position:
    def __init__(self, number, input_list) -> None:
        self.number = number
        self.crab_list = input_list
        self.total_fuel_1 = self.total_crab_fuel(self.crab_list, "standard")
        self.total_fuel_2 = self.total_crab_fuel(self.crab_list, "increasing")

    def find_crab_fuel(self, crab_position, method):
        if method == "standard":
            return max(crab_position, self.number) - min(crab_position, self.number)
        elif method == "increasing":
            running_total = 0
            moves = max(crab_position, self.number) - min(crab_position, self.number)
            for num in range(1, moves + 1):
               running_total += num
            return running_total
        else:
            return ValueError
    
    def total_crab_fuel(self, input_list, method):
        total = 0
        for crab in input_list:
            total += self.find_crab_fuel(crab, method)         
        return total

def find_all_fuels(input_list, method):
    fuel_dict = {}
    sorted_list = sorted(input_list)
    for num in range(sorted_list[0], sorted_list[-1] + 1):
        this_position = Position(num, input_list)
        if method == "standard":
            fuel_dict[num] = this_position.total_fuel_1
        elif method == "increasing":
            fuel_dict[num] = this_position.total_fuel_2
        else:
            return ValueError
    return fuel_dict

#print(full_dictionary_2)

def find_lowest_fuel(input_dict):
    lowest_fuel = min(input_dict.values())
    for key, value in input_dict.items():
        if value == lowest_fuel:
            return [key, value]

print(datetime.datetime.now())
full_dictionary_1 = find_all_fuels(working_list, "standard")
lowest = find_lowest_fuel(full_dictionary_1)
print(lowest)
print(datetime.datetime.now())
#full_dictionary_2 = find_all_fuels(working_list, "increasing")
#lowest2 = find_lowest_fuel(full_dictionary_2)
#print(lowest2)
print(datetime.datetime.now())





        