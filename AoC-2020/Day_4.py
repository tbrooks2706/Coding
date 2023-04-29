import general_functions
from copy import deepcopy

#https://adventofcode.com/2020/day/4

########THIS WOULD MAKE GOOD UNIT TEST PRACTICE########################
class Field:
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional = ["cid"]
    hcl_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    ecl_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    byr_min = 1920
    byr_max = 2002
    iyr_min = 2010
    iyr_max = 2020
    eyr_min = 2020
    eyr_max = 2030
    hgt_in_min = 59
    hgt_in_max = 76
    hgt_cm_min = 150
    hgt_cm_max = 193
    yr_len = 4
    pid_len = 9
    hcl_len = 7

    def __init__(self, field_name, field_value) -> None:
        self.name = field_name
        self.value = field_value
        self.required = field_name in Field.required
        self.valid = self.check_validity()

    def check_validity(self):
            if self.value in (None, "") and self.required == True:
                return False
            if self.name == "byr":
                num_byr = int(self.value)
                if Field.byr_min <= num_byr <= Field.byr_max and len(self.value) == Field.yr_len:
                    return True
                return False
            if self.name == "iyr":
                num_iyr = int(self.value)
                if Field.iyr_min <= num_iyr <= Field.iyr_max and len(self.value) == Field.yr_len:
                    return True
                return False
            if self.name == "eyr":
                num_eyr = int(self.value)
                if Field.eyr_min <= num_eyr <= Field.eyr_max and len(self.value) == Field.yr_len:
                    return True
                return False
            if self.name == "hgt":
                #exception handling for if value doesn't follow the "some digits then two letters" format eg. it's just the digits
                try:
                    unit = self.value[-2:]
                    num_hgt = int(self.value[:-2])
                except:
                    return False
                else:
                    if unit == "cm" and Field.hgt_cm_min <= num_hgt <= Field.hgt_cm_max:
                        return True
                    if unit == "in" and Field.hgt_in_min <= num_hgt <= Field.hgt_in_max:
                        return True
                    return False
            if self.name == "hcl":
                if self.value[0] == "#" and len(self.value) == Field.hcl_len:
                    counter = 0
                    for char in self.value[1:]:
                        if char in Field.hcl_chars:
                            counter += 1
                    if counter == 6:
                        return True
                return False
            if self.name == "ecl":
                if self.value in Field.ecl_values:
                    return True
                return False
            if self.name == "pid":
                if len(self.value) == Field.pid_len:
                    #test to see whether string is all digits
                    try:
                        num = int(self.value)
                    #if not, field invalid
                    except:
                        return False
                    #if no exception thrown, field valid
                    else:
                        return True
                return False
            if self.name == "cid":
                return True     

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
        self.valid_1 = self.check_validity_1()
        self.valid_2 = self.check_validity_2()
    
    def check_validity_1(self):
        for field, value in self.full_dict.items():
            this_field = Field(field, value)
            if this_field.required == True and value == None:
                return False
        return True
    
    def check_validity_2(self):
        for field, value in self.full_dict.items():
            this_field = Field(field, value)
            if this_field.valid == False:
                return False
        return True

def count_valid_passports(input_list):
    counter = 0
    for item in input_list:
        this_passport = Passport(item)
        if this_passport.valid_2 == True:
            counter += 1
    return counter

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

working_list = read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2020\Day_4.txt")

#adjust if statement in count_valid_passports, to switch between part 1 and 2 answers
valid_count = count_valid_passports(working_list)
print(valid_count)