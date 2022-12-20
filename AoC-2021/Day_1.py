import general_functions

class Measurement:
    def __init__(self, input_list, list_index):
        self.input_list = input_list
        self.list_index = list_index
        self.depth = int(input_list[list_index])
        self.previous_depth = int(input_list[list_index - 1])
        self.larger_than_previous = self.depth > self.previous_depth
    
    def three_increase(self):
        self.current_three = int(self.input_list[self.list_index]) + int(self.input_list[self.list_index + 1]) + int(self.input_list[self.list_index + 2])
        self.previous_three = int(self.input_list[self.list_index - 1]) + int(self.input_list[self.list_index]) + int(self.input_list[self.list_index + 1])
        return self.current_three > self.previous_three

def number_of_increases(input_list):
    counter = 0
    for num in range(1, len(input_list)):
        this_measure = Measurement(input_list, num)
        if this_measure.larger_than_previous == True:
            counter += 1
    return counter

def number_of_three_increases(input_list):
    counter = 0
    for num in range(1, len(input_list) - 2):
        this_measure = Measurement(input_list, num)
        if this_measure.three_increase() == True:
            counter += 1
    return counter

init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_1.txt")
test_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_1_test.txt")

#answer to part 1
print(number_of_increases(init_list))

#answer to part 2
print(number_of_three_increases(init_list))