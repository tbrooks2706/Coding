import general_functions
import math
from copy import deepcopy

#https://adventofcode.com/2020/day/5

#no test file - it's just one 10-char string

#input = list of boarding passes
#characters in string are F front, B back, L left, R right
#first 7 characters will either be F or B - they specify the row 0-127
    #B means take upper half, L means lower half
#each character halves the available seats in the region being considered, till it's narrowed down to 1 row
#last 3 characters will either be L or R - they specify the column 0-7
    #R means take upper half, L means lower half

#parameterise number of rows and columns

class Plane:
    first_row = 0
    last_row = 127
    first_column = 0
    last_column = 7

    def __init__(self, pass_list) -> None:
        self.seat_plan_blank = self.create_seat_plan()
        self.pass_list = pass_list

    def create_seat_plan(self):
        row = [None, None, None, None, None, None, None, None]
        dct = {}
        #create dict with numbers and blank lists
        for num in range(128):
            dct[num] = row
        #print(dct)
        return dct
    
    ###FINISH THIS THEN DO FUNCTION BELOW TO FIND BLANKS###
    def populate_seat_plan(self):
        for string in self.pass_list:
            pass
    
class BoardingPass:
    def __init__(self, string) -> None:
        self.string = string
        self.start_rows = [Plane.first_row, Plane.last_row]
        self.start_columns = [Plane.first_column, Plane.last_column]
        self.row = self.calculate_row()
        self.column = self.calculate_column()
        self.seat_id = self.calculate_seat_id()
    
    def calculate_seat_id(self):
        try:
            return (self.row * 8) + self.column
        except:
            return "Invalid row or column"
        
    def calculate_row(self):
        current_rows = deepcopy(self.start_rows)
        for char in self.string[:7]:
            if char == "B":
                new_rows = self.keep_top_half(current_rows)
            else:
                new_rows = self.keep_bottom_half(current_rows)
            current_rows = new_rows
            if isinstance(current_rows, int):
                break
        return current_rows

    def calculate_column(self):
        current_columns = deepcopy(self.start_columns)
        for char in self.string[7:]:
            if char == "R":
                new_columns = self.keep_top_half(current_columns)
            else:
                new_columns = self.keep_bottom_half(current_columns)
            current_columns = new_columns
            if isinstance(current_columns, int):
                break
        return current_columns
    
    def keep_top_half(self, input):
        diff = input[1] - input[0]
        top = input[1]
        bottom = top - math.floor(diff / 2)
        if bottom == top:
            return top
        return [bottom, top]

    def keep_bottom_half(self, input):
        bottom = input[0]
        diff = input[1] - input[0]
        top = bottom + math.floor(diff / 2)
        if bottom == top:
            return top
        return [bottom, top]   

# tests = [[0, 127], [0, 63], [32, 63], [32, 47], [40, 47], [44, 47], [44, 45]]
# e_top = [[64, 127], [32, 63], [48, 63], [40, 47], [44, 47], [46, 47], 45]
# e_btm = [[0, 63], [0, 31], [32, 47], [32, 39], [40, 43], [44, 45], 44]

# for num in range(len(tests)):
#     test = tests[num]
#     expected = e_top[num]
#     actual = keep_top_half(tests[num])
#     result = expected == actual
#     print("Test:", test, ", Expected:", expected, ", Actual:", actual, "Result:", result)

# string = "BBFFBBFRLL"
# example_pass = BoardingPass(string)
# print_output = [string, example_pass.row, example_pass.column, example_pass.seat_id]
# print_string = "Boarding Pass: %s, Row: %d, Column: %d, SeatID: %d"
# print(print_string % (string, example_pass.row, example_pass.column, example_pass.seat_id))

def highest_seat_id(input_list):
    id = 0
    for string in input_list:
        this_pass = BoardingPass(string)
        if this_pass.seat_id > id:
            id = this_pass.seat_id
    return id

def find_my_seat(input_list):
    this_plane = Plane(input_list)

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2020\Day_5.txt")

#answer part 1
part_1 = highest_seat_id(init_list)
print(part_1)

#answer part 2
part_2 = find_my_seat(init_list)
print(part_2)