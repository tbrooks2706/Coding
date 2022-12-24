import general_functions
import copy

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_4.txt")
test_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_4_test.txt")
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
        self.number_called = 0
        self.seq = 0
        self.score = 0
    
    def create_columns(self):
        column_list = []
        for num in range(len(self.row_list[0])):
            column = []
            for row in self.row_list:
                column.append(row[num])
            column_list.append(column)
        return column_list

    def mark_board(self, number):
        new_list = copy.deepcopy(self.row_list)
        for row in new_list:
            for index in range(len(row)):
                if row[index] == number:
                    row[index] = "#"+row[index]
        self.row_list = new_list
        self.column_list = self.create_columns()
        self.number_called = int(number)
        self.seq += 1
    
    def count_marked(self):
        column_marked = []
        row_marked = []
        for column in self.column_list:
            count = 0
            for value in column:
                if "#" in value:
                    count += 1
            column_marked.append(count)
        for row in self.row_list:
            count = 0
            for value in row:
                if "#" in value:
                    count += 1
            row_marked.append(count)
        return [row_marked, column_marked]

    def sum_values(self):
        sum = 0
        unmarked = 0
        marked = 0
        #print(self.column_list)
        for row in self.row_list:
            for value in row:
                #print(value)
                if "#" not in value:
                    unmarked += int(value)
                    sum += int(value)
                else:
                    marked += int(value[1:])
                    sum += int(value[1:])
        return [sum, unmarked, marked]

example_board = Board([['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']])
for num in ["1", "21", "17", "2"]:
    example_board.mark_board(num)
#print(example_board.row_list)
print(example_board.count_marked())
print("unmarked",example_board.sum_values()[1])
print("marked",example_board.sum_values()[2])
print("total",example_board.sum_values()[0])
print("seq",example_board.seq)
print("number called",example_board.number_called)
print("score",example_board.number_called * example_board.sum_values()[1])

#not sure if we need this class
class Number_Draw:
    def __init__(self, number, seq) -> None:
        self.number = number
        self.seq = seq

#for each number draw
    #go through entire list, and mark each board
    #check number marked on each board, if any 5, break
    #for that board, output sum unmarked * number most recently called
#OR
#for each board
    #go through number list, mark board while no row or column = 5
    #when loop finished, do next board
#then find board which has the lowest seq value, and output score for it

