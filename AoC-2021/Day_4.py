import general_functions
import copy

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_4.txt")
test_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_4_test.txt")
#print(test_list)
draw_order = test_list[0].split(",")
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
        board_win = False
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
        if (5 in row_marked) or (5 in column_marked):
            board_win = True
        return [row_marked, column_marked, board_win]

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

#example_board = Board([['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']])
#example_board = Board(boards[0:5])
#for num in ["21", "8", "22", "1", "5"]:
#    example_board.mark_board(num)
#print(example_board.row_list)
#print(example_board.count_marked())
#print("unmarked",example_board.sum_values()[1])
#print("marked",example_board.sum_values()[2])
#print("total",example_board.sum_values()[0])
#print("seq",example_board.seq)
#print("number called",example_board.number_called)
#print("score",example_board.number_called * example_board.sum_values()[1])

class Number_Draw:
    def __init__(self, number) -> None:
        self.number = number

    def mark_all_numbers(self, input_boards):
        #go through each line, mark the number if it's there, then overwrite that line the original list (boards) with the new line
        for line in input_boards:
            for index in range(len(line)):
                if line[index] == self.number:
                    line[index] = "#"+line[index]

#example_number_draw = Number_Draw("10")
#example_number_draw.mark_all_numbers(boards)
#print(boards)

        
class Boards_List:
    def __init__(self, input_list) -> None:
        self.boards_list = input_list
        self.board_starts = self.determine_board_starts()

    def determine_board_starts(self):
        starts_list = []
        for x in range(len(self.boards_list)):
            if x % 6 == 0:
                starts_list.append(x)
        return starts_list

example_boards_list = Boards_List(boards)
#print(example_boards_list.board_starts)

#for each number draw
    #go through entire list, and mark each board
    #check number marked on each board, if any 5, break
    #for that board, output sum unmarked * number most recently called
#OR
#for each board
    #go through number list, mark board while no row or column = 5
    #when loop finished, do next board
#then find board which has the lowest seq value, and output score for it

def get_winning_board(draw_list, board_list):
    start_points = Boards_List(board_list).board_starts
    end_now = False
    winning_board = 0
    for draw in draw_list:
        this_draw = Number_Draw(draw)
        this_draw.mark_all_numbers(board_list)
        for num in range(len(board_list)):
            if num in start_points:
                this_board = Board(board_list[num:num+5])
                if this_board.count_marked()[2] == True:
                    end_now = True
                    winning_board = num
                    winning_score = this_board.sum_values()[1] * int(draw)
        if end_now == True:
            break
    return {"board start": winning_board, "score": winning_score}

def get_losing_board(draw_list, board_list):
    start_points = Boards_List(board_list).board_starts
    end_now = False
    losing_board = 0
    completed_boards = []
    for draw in draw_list:
        this_draw = Number_Draw(draw)
        this_draw.mark_all_numbers(board_list)
        for num in range(len(board_list)):
            print(num)
            if (num in start_points) and (num not in completed_boards):
                this_board = Board(board_list[num:num+5])
                if this_board.count_marked()[2] == True:
                    completed_boards.append([num, draw])
                    print(completed_boards)
                    print(start_points)
                    continue
                    #end_now = True
        if len(completed_boards) == len(start_points):
            break
    losing_board = completed_boards[-1]
    #new_board = Board(board_list[losing_board:losing_board+5])
    #losing_score = new_board.sum_values()[1] * int(draw)
    #return {"board start": losing_board, "score": losing_score}

winning_board = get_winning_board(draw_order, boards)
losing_board = get_losing_board(draw_order, boards)
#answer to part 1
print(winning_board)

