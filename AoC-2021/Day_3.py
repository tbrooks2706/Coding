import general_functions
import copy

class Column:
    def __init__(self, input_list, index) -> None:
        self.input_list = input_list
        self.index = index
        self.column = self.create_column()
        if self.column.count("0") > self.column.count("1"):
            self.gamma = "0"
            self.epsilon = "1"
        else:
            self.gamma = "1"
            self.epsilon = "0"
        
    def create_column(self):
        column = ""
        for item in self.input_list:
            column += item[self.index]
        return column

#part 1
def compile_binaries(input_list):
    gamma = ""
    epsilon = ""
    for num in range(len(input_list[0])):
        this_column = Column(input_list, num)
        gamma += this_column.gamma
        epsilon += this_column.epsilon
    return [gamma, epsilon]

#part 2
def find_rating(input_list, search_type):
    new_list = copy.deepcopy(input_list)
    column_index = 0
    while len(new_list) > 1:
        temp_list = []
        this_column = Column(new_list, column_index)
        for row in new_list:
            if search_type == "oxygen":
                if row[column_index] == this_column.gamma:
                    temp_list.append(row)
            else:
                if row[column_index] == this_column.epsilon:
                    temp_list.append(row)
        column_index += 1
        new_list = temp_list
    return new_list[0]

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_3.txt")
test_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_3_test.txt")

#answer part 1
binary_list = compile_binaries(init_list)
gamma_rate = int(binary_list[0], 2)
epsilon_rate = int(binary_list[1], 2)
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)

#answer part 2
oxygen_rating = int(find_rating(init_list, "oxygen"),2)
CO2_rating = int(find_rating(init_list, "CO2"),2)
life_support_rating = oxygen_rating * CO2_rating
print(life_support_rating)