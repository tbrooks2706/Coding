import copy

#numbers are a heightmap of the ocean floor
#9 highest 0 lowest
#low point = number that's lower than all adjacent points (up down left right)
#risk level = height + 1

with open(r"c:/Users/Tom.Brooks/OneDrive - BJSS Ltd/Documents/Coding/Coding/AoC-2021\Day_9_test.txt") as input_file:
    init_list = []
    working_list = []
    for row in input_file:
        init_list.append(row.replace("\n",""))
    for item in init_list:
        temp_list = []
        for char in item:
            temp_list.append(int(char))
        working_list.append(temp_list)
#print(working_list)
part_2_list = copy.deepcopy(working_list)
print(part_2_list)

class Point:
    def __init__(self, grid, row, column) -> None:
        self.row = row
        self.column = column
        self.grid = grid
        self.height = grid[row][column]
        self.risk = self.height + 1
        self.last_row = self.row == len(grid) - 1
        self.last_column = self.column == len(grid[0]) - 1
        self.up = lambda: self.grid[self.row-1][self.column] if self.row != 0 else 99
        self.down = lambda: self.grid[self.row+1][self.column] if not self.last_row else 99
        self.left = lambda: self.grid[self.row][self.column-1] if self.column != 0 else 99
        self.right = lambda: self.grid[self.row][self.column+1] if not self.last_column else 99
        self.adjacents = [self.up(), self.down(), self.left(), self.right()]
        self.low_point = lambda: True if self.height < min(self.adjacents) else False

example_point = Point(working_list, 0, 0)
#print(example_point.adjacents)
#print(example_point.low_point())

def sum_risk(input_list):
    running_total = 0
    row_ind = 0
    for row in input_list:
        column_ind = 0
        for num in row:
            this_point = Point(working_list, row_ind, column_ind)
            if this_point.low_point() == True:
                running_total += this_point.risk
            column_ind += 1
        row_ind += 1
    return running_total

#answer part 1
part_1 = sum_risk(working_list)
print(part_1)

#give each low point a separate number, then made it spread its own number until it hit a wall
# def apply_low_point_ids(input_list):
#     target_id = 101
#     for row in input_list:
#         column_ind = 0
#         for num in row:
#         #     this_point = Point(working_list, row_ind, column_ind)
#         #     if this_point.low_point() == True:
#         #         running_total += this_point.risk
#         #     column_ind += 1
#         # row_ind += 1

# def spread_number(input_list):
#     running_total = 0
#     row_ind = 0
#     for row in input_list:
#         column_ind = 0
#         for num in row:
#             this_point = Point(working_list, row_ind, column_ind)
#             if this_point.low_point() == True:
#                 running_total += this_point.risk
#             column_ind += 1
#         row_ind += 1
#     return running_total

#if it's a low point, change its number in the original grid list to be 101, 102, 103 etc
    #then can identify them using numbers > 100
#make it spread its own number till it hits a wall
    #for each number >100, look in all four directions and change any that aren't 9 to match it
    #then repeat for the same number, until there are no new numbers to spread to
#count the numbers of each number above 100, to find the size of each basin (dictionary?)
#sort the values in the dictionary and count the three biggest ones