import general_functions
from copy import deepcopy

#https://adventofcode.com/2020/day/4

# init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2020\Day_4_test.txt")
# print(init_list)

# #format data
# def format_batch_file(input_list):
#     new_list = []
#     for line in input_list:
#         new_list.append(line.split())
#     #range starts at 1 to skip first line
#     for num in range(1, len(new_list)):
#         counter = 0
#         while counter < 1:
#             if new_list[num] != [] and new_list[num-1] != []:
#                 new_list[num-1] += new_list[num]
#                 new_list.pop(num)
#                 counter += 1
#             else:
#                 pass
#                 counter += 1
#     return new_list

#working_list = format_batch_file(init_list)
#print(working_list)

def read_file(file_path):
    with open(file_path) as txt_file:
        #one big list, lines only
        init_list = []
        for line in txt_file:
            init_list.append(line.split())
        new_list = [[]]
        ind = 0
        #group fields together by passport
        for line in init_list:
            if line != []:
                for field in line:
                    new_list[ind].append(field)
            else:
                ind += 1
                new_list.append([])
        dict_list = []
        #convert passport groups into dictionaries
        for line in new_list:
            dct = {}
            for field in line:
                split = field.split(":")
                dct[split[0]] = split[1]
            dict_list.append(dct)
    return dict_list

working_list = read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2020\Day_4_test.txt")
#print(working_list)

#count valid passports in batch file (input)
#valid = contains all required fields (byr, iyr, eyr, hgt, hcl, ecl, pid)
#temporarily ignore missing cid fields - treat it as optional
#passports in file separated by blank lines

#parameterise whether fields are optional or not

#############PART 2 INVOLVES FIELD SPECIFIC VALIDATION#################
class Field:
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional = ["cid"]

    def __init__(self, field_name) -> None:
        self.name = field_name
        self.required = field_name in Field.required

class Passport:
    def __init__(self, input_dict) -> None:
        self.input_dict = input_dict
        self.byr = input_dict.get("byr")
        self.iyr = input_dict.get("iyr")
        self.eyr = input_dict.get("eyr")
        self.hgt = input_dict.get("hgt")
        self.hcl = input_dict.get("hcl")
        self.ecl = input_dict.get("ecl")
        self.pid = input_dict.get("pid")
        self.cid = input_dict.get("cid")
        self.full_dict = {'byr': self.byr, 'iyr': self.iyr, 'eyr': self.eyr, 'hgt': self.hgt, 'hcl': self.hcl, 'ecl': self.ecl, 'pid': self.pid, 'cid': self.cid}
        self.valid = self.check_validity()
    
    def check_validity(self):
        for field, value in self.full_dict.items():
            this_field = Field(field)
            if this_field.required == True and value == None:
                return False
        return True

# example_passport = Passport({'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'})
# print(example_passport.full_dict)
# print(example_passport.valid)

def count_valid_passports(input_list):
    counter = 0
    for item in input_list:
        this_passport = Passport(item)
        if this_passport.valid == True:
            counter += 1
    return counter

#part 1 answer
valid_count_1 = count_valid_passports(working_list)
print(valid_count_1)

