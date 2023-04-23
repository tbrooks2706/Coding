#input is list of passwords according to corrupted database
#first bit before colon is password policy (eg. 1-3 a means pass needs to contain 1-3 "a" chars)
#second bit after colon is password
#how many passwords in the input are valid?

import general_functions

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2020\Day_2_test.txt")

def format_list(input_list):
    new_list = []
    for string in input_list:
        temp_list = string.split("-")
        temp_list.append(temp_list[1].split(" ",1))
        temp_list.append(temp_list[2][1][0:1])
        temp_list.append(temp_list[2][1][3:])
        clean = [int(temp_list[0]), int(temp_list[2][0]), temp_list[3], temp_list[4]]
        new_list.append(clean)
    return new_list

working_list = format_list(init_list)
print(working_list)
