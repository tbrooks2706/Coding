#this is a set of reusable functions

#opening input file and putting it in a list
def read_file(file_path):
    with open(file_path) as txt_file:
        init_list = []
        for line in txt_file:
            init_list.append(line.replace("\n", ""))
    return init_list

def reverse_string(string):
    return string[::-1]

def create_grid(width, height):
    grid = []
    for num in range(width):
        column = []
        for num in range(height):
            column.append(".")
        grid.append(column)
    return grid

def create_blank_list(char, num_of_chars):
    new_list = []
    for x in range(num_of_chars):
        new_list.append(char)
    return new_list

def check_for_duplicates(input_list):
    duplicates = len(input_list) - len(set(input_list))
    if duplicates == 0:
        return "No duplicates"
    else:
        return "{num} duplicates".format(num = duplicates)