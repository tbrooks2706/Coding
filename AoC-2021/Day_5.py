import general_functions

class Grid:
    def __init__(self, width, height) -> None:
        self.grid = general_functions.create_grid(width, height)
        self.width = width
        self.height = height
        self.intersections = 0

    def mark_point(self, coordinates):
        x = coordinates[0]
        y = coordinates[1]
        if self.grid[x][y] == ".":
            self.grid[x][y] = 1
        else:
            self.grid[x][y] += 1
    
    def count_intersections(self):
        intersections = 0
        for column in self.grid:
            for point in column:
                if (type(point) == int) and (point > 1):
                    intersections += 1
        return intersections

class Line:
    def __init__(self, points) -> None:
        self.start_x = min(points[0], points[2])
        self.start_y = min(points[1], points[3])
        self.end_x = max(points[0], points[2])
        self.end_y = max(points[1], points[3])
        self.input_points = points
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
    
    #returns list of x,y points that will be marked for this line
    def find_points_on_line(self):
        points_list = []
        if self.is_horizontal == True:
            for num in range(self.start_x, self.end_x + 1):
                points_list.append([num, self.start_y])
        elif self.is_vertical == True:
            for num in range(self.start_y, self.end_y + 1):
                points_list.append([self.start_x, num])
        else:
            #diagonals
            if (self.input_points[0] < self.input_points[2]) and (self.input_points[1] < self.input_points[3]):
            #top left to bottom right - normal
                x = self.input_points[0]
                y = self.input_points[1]
                for num in range(self.input_points[0], self.input_points[2] + 1):
                    points_list.append([x, y])
                    x += 1
                    y += 1
            elif (self.input_points[0] > self.input_points[2]) and (self.input_points[1] > self.input_points[3]):
            #top left to bottom right - reversed
                x = self.input_points[2]
                y = self.input_points[3]
                for num in range(self.input_points[2], self.input_points[0] + 1):
                    points_list.append([x, y])
                    x += 1
                    y += 1
            elif (self.input_points[0] > self.input_points[2]) and (self.input_points[1] < self.input_points[3]):
            #top right to bottom left - normal
                x = self.input_points[0]
                y = self.input_points[1]
                for num in range(self.input_points[1], self.input_points[3] + 1):
                    points_list.append([x, y])
                    x -= 1
                    y += 1
            else:
            #top right to bottom left - reversed
                x = self.input_points[0]
                y = self.input_points[1]
                for num in range(self.input_points[0], self.input_points[2] + 1):
                    points_list.append([x, y])
                    x += 1
                    y -= 1
        return points_list

#converts input list of strings into usable nested lists of integers
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

#returns a new list with horizontal and vertical lines only
def remove_diagonals(input_list):
    new_list = []
    for line in input_list:
        this_line = Line(line)
        if this_line.is_diagonal == False:
            new_list.append(line)
    return new_list

#marks all lines on a given grid        
def mark_lines(input_grid, list_of_lines):
    for line in list_of_lines:
        this_line = Line(line)
        for point in this_line.points_list:
            input_grid.mark_point(point)

#execute code
init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_5.txt")
test_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_5_test.txt")
working_list = format_list(init_list)
filtered_list = remove_diagonals(working_list)
test_grid = Grid(10, 10)        
grid_part_one = Grid(1000, 1000)
grid_part_two = Grid(1000, 1000)
mark_lines(grid_part_one, filtered_list)
mark_lines(grid_part_two, working_list)

#answer part 1
print(grid_part_one.count_intersections())

#answer part 2
print(grid_part_two.count_intersections())