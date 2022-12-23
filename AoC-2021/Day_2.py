import general_functions

class Move:
    def __init__(self, move) -> None:
        self.direction = move.split()[0]
        self.number = int(move.split()[1])

#part 1
def calculate_position_a(input_list):
    depth = 0
    horizontal = 0
    for item in input_list:
        this_move = Move(item)
        if this_move.direction == "forward":
            horizontal += this_move.number
        elif this_move.direction == "up":
            depth -= this_move.number
        else:
            depth += this_move.number
    return depth * horizontal

#part 2
def calculate_position_b(input_list):
    depth = 0
    horizontal = 0
    aim = 0
    for item in input_list:
        this_move = Move(item)
        if this_move.direction == "forward":
            horizontal += this_move.number
            depth += (this_move.number * aim)
        elif this_move.direction == "up":
            aim -= this_move.number
        else:
            aim += this_move.number
    return depth * horizontal

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_2.txt")
test_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_2_test.txt")

#answer part 1
print(calculate_position_a(init_list))

#answer part 2
print(calculate_position_b(init_list))