import general_functions
import copy

init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_5.txt")
test_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_5_test.txt")
working_grid = general_functions.create_grid(10, 10)

class Line:
    def __init__(self, points) -> None:
        self.start_x = points[0]
        self.start_y = points[1]
        self.end_x = points[2]
        self.end_y = points[3]
        self.is_diagonal = self.set_direction()[0]
        self.is_horizontal = self.set_direction()[1]
        self.is_vertical = self.set_direction()[2]
    
    def set_direction(self):
        is_diagonal = False
        is_vertical = False
        is_horizontal = False
        if (self.start_x != self.end_x) and (self.start_y != self.end_y):
            is_diagonal = True
        elif (self.start_x == self.end_x):
            is_horizontal = True
        else:
            is_vertical = True
        return [is_diagonal, is_horizontal, is_vertical]
    
    ##############make this function next#################
    def find_points_on_line(self):
        pass
example_line = Line([0,9,5,9])
print(example_line.is_diagonal)

def format_list(input_list):
    new_list = []
    final_list = []
    for line in input_list:
        x = line.split(" -> ")
        new_list.append(x)
    for line in new_list:
        temp_list = []
        for point in line:
            a = point.split(",")
            temp_list.append(int(a[0]))
            temp_list.append(int(a[1]))
        final_list.append(temp_list)
    return final_list

def remove_diagonals(input_list):
    new_list = []
    for line in input_list:
        this_line = Line(line)
        if this_line.is_diagonal == False:
            new_list.append(line)
    return new_list

working_list = format_list(test_list)
#print(working_list)
filtered_list = remove_diagonals(working_list)
print(filtered_list)
        
#then mark lines on grid

#count number of points >1