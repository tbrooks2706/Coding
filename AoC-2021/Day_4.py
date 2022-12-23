import general_functions

init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_4.txt")
test_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_4_test.txt")
#print(test_list)
draw_order = init_list[0].split(",")
#print(general_functions.check_for_duplicates(draw_order))
boards = [item.split() for item in test_list[2:]]
#print(draw_order)
#print(boards)

#numbers are marked on all boards on which they appear, when drawn
#if any row or column in a board is completed, that board wins
#OUTPUT score of winning board = sum of all unmarked numbers on it * number that was just called when it won

class Board:
    def __init__(self, row_list) -> None:
        self.row_list = row_list
        self.column_list = self.create_columns()
    
    def create_columns(self):
        column_list = []
        for num in range(len(self.row_list[0])):
            column = []
            for row in self.row_list:
                column.append(row[num])
            column_list.append(column)
        return column_list

    def mark_board(self, number):
        for row in self.row_list:
            for index in range(len(row)):
                if row[index] == number:
                    row[index] = "#"+row[index]
        return self.row_list


example_board = Board([['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']])
print(example_board.mark_board("22"))

class Number_Draw:
    def __init__(self, number, seq) -> None:
        self.number = number
        self.seq = seq

