#input is list of passwords according to corrupted database
#first bit before colon is password policy (eg. 1-3 a means pass needs to contain 1-3 "a" chars)
#second bit after colon is password
#how many passwords in the input are valid?

import general_functions

class Password:
    def __init__(self, input_list) -> None:
        self.password = input_list[3]
        self.pass_char = input_list[2]
        self.min_char = input_list[0]
        self.max_char = input_list[1]
        self.check_index = [self.min_char - 1, self.max_char - 1]
        self.is_valid_one = self.check_valid_one()
        self.is_valid_two = self.check_valid_two()

    def check_valid_one(self):
        char_count = self.password.count(self.pass_char)
        if self.min_char <= char_count <= self.max_char:
            return True
        return False
    
    def check_valid_two(self):
        match_count = 0
        for ind in self.check_index:
            if self.password[ind] == self.pass_char:
                match_count += 1
        if match_count == 1:
            return True
        return False

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

def count_valid(input_list):
    counter = [0, 0]
    for pwd in input_list:
        this_password = Password(pwd)
        if this_password.is_valid_one == True:
            counter[0] += 1
        if this_password.is_valid_two == True:
            counter[1] += 1
    return counter

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2020\Day_2.txt")
working_list = format_list(init_list)

answer_part_1 = count_valid(working_list)[0]
print(answer_part_1)

answer_part_2 = count_valid(working_list)[1]
print(answer_part_2)