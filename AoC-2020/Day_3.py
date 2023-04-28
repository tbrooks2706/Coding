import general_functions
from copy import deepcopy

#https://adventofcode.com/2020/day/3

#find which angles will take you near the fewest trees
#input is a map of trees and open squares
# # = tree square, . = open square
#toboggan can only follow a few specific slopes - it can only do rational numbers eg 3 down 2 right
#tree pattern on map repeats infinitely to the right
    #infinitely = for as many repetitions as needed for the slope line to hit the bottom of the map
#count how many trees you would encounter on the line R3D1, from start 0,0

class Slope:
    def __init__(self, start_point, slope_right, slope_down, input_list) -> None:
        self.start_point = start_point
        self.start_x = start_point[0]
        self.start_y = start_point[1]
        self.slope_right = slope_right
        self.slope_down = slope_down
        self.grid = input_list
        self.number_of_columns = len(input_list[0])
        self.squares_checked = self.points_to_check()
        self.trees_hit = self.count_trees()
        
    def points_to_check(self):
        coordinates = deepcopy(self.start_point)
        row = coordinates[1] + self.slope_down
        column = coordinates[0] + self.slope_right
        checked = []
        #loop to work out the list of coordinates in advance
        while row < len(self.grid):
            checked.append([column % self.number_of_columns, row])
            row += self.slope_down
            column += self.slope_right
        return checked
    
    def count_trees(self):
        counter = 0
        for point in self.squares_checked:
            #retrieve space value based on grid coordinates
            space = self.grid[point[1]][point[0]]
            if space == "#":
                counter += 1
        return counter

def count_trees_for_slope(start_point=[0,0], slope_right=0, slope_down=0, input_list=[]):
    this_slope = Slope(start_point, slope_right, slope_down, input_list)
    return this_slope.trees_hit

def multiply_several_slopes(list_of_slopes):
    slope_counts = []
    multiply_result = 1
    for x in list_of_slopes:
        slope_counts.append(count_trees_for_slope([0,0], x[0], x[1], init_list))
    for count in slope_counts:
        multiply_result *= count
    return multiply_result

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2020\Day_3.txt")

#part 1 answer
slope_part_1 = count_trees_for_slope([0,0], 3, 1, init_list)
print(slope_part_1)

#part 2 answer
slope_part_2 = multiply_several_slopes([[1,1],[3,1],[5,1],[7,1],[1,2]])
print(slope_part_2)