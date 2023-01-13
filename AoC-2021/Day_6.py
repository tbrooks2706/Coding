import general_functions
from collections import defaultdict

#Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.
#how many lanternfish after 18 days(test only)? after 80 days?

def format_list(raw_list):
    new_list = raw_list[0].split(",")
    for index in range(len(new_list)):
        new_list[index] = int(new_list[index])
    return new_list

def create_fish_map(input_list):
    fish_map = {}
    for fish in input_list:
        if fish not in fish_map.keys():
            fish_map[fish] = 0
        fish_map[fish] += 1
    return fish_map

def pass_time(input_dict, number_of_days):
    fish_dict = input_dict
    for day in range(number_of_days):
        updated_fish_map = defaultdict(int)
        for fish, count in fish_dict.items():
            if fish == 0:
                updated_fish_map[8] += count
                updated_fish_map[6] += count
            else:
                updated_fish_map[fish - 1] += count
        fish_dict = updated_fish_map
    return fish_dict

#execute code
init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_6.txt")
test_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_6_test.txt")
working_list = format_list(init_list)
fish_map = create_fish_map(working_list)

#answer part 1
end_map_1 = pass_time(fish_map, 80)
fish_1 = sum(end_map_1.values())
print(fish_1)

#answer part 2
end_map_2 = pass_time(fish_map, 256)
fish_2 = sum(end_map_2.values())
print(fish_2)