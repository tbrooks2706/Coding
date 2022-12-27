import general_functions
import copy

init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_5.txt")
test_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_5_test.txt")

class Grid:
    def __init__(self, width, height) -> None:
        self.grid = general_functions.create_grid(width, height)
        self.width = width
        self.height = height

    def mark_point(self, coordinates):
        x = coordinates[0]
        y = coordinates[1]
        if self.grid[x][y] == ".":
            self.grid[x][y] = 1
        else:
            self.grid[x][y] += 1
        
working_grid = Grid(10, 10)
working_grid.mark_point([0,2])
working_grid.mark_point([7,0])
print(working_grid.grid)


class Line:
    def __init__(self, points) -> None:
        self.start_x = min(points[0], points[2])
        self.start_y = min(points[1], points[3])
        self.end_x = max(points[0], points[2])
        self.end_y = max(points[1], points[3])
        self.is_diagonal = self.set_direction()[0]
        self.is_horizontal = self.set_direction()[1]
        self.is_vertical = self.set_direction()[2]
        self.points_list = self.find_points_on_line()
    
    def set_direction(self):
        is_diagonal = False
        is_vertical = False
        is_horizontal = False
        if (self.start_x != self.end_x) and (self.start_y != self.end_y):
            is_diagonal = True
        elif (self.start_x == self.end_x):
            is_vertical = True
        else:
            is_horizontal = True
        return [is_diagonal, is_horizontal, is_vertical]
    
    def find_points_on_line(self):
        points_list = []
        if self.is_horizontal == True:
            for num in range(self.start_x, self.end_x + 1):
                points_list.append([num, self.start_y])
        if self.is_vertical == True:
            for num in range(self.start_y, self.end_y + 1):
                points_list.append([num, self.start_x])
        return points_list

example_line = Line([7,0,7,4])
#print(example_line.is_horizontal)
#print(example_line.start_y)
#print(example_line.find_points_on_line())

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
def mark_lines(input_grid, list_of_lines):
    for line in list_of_lines:
        this_line = Line(line)


#count number of points >1