import general_functions

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
        for row in self.row_list:
            for value in row:
                if "#" not in value:
                    unmarked += int(value)
                    sum += int(value)
                else:
                    marked += int(value[1:])
                    sum += int(value[1:])
        return [sum, unmarked, marked]

class Number_Draw:
    def __init__(self, number) -> None:
        self.number = number

    def mark_all_numbers(self, input_boards):
        for line in input_boards:
            for index in range(len(line)):
                if line[index] == self.number:
                    line[index] = "#"+line[index]
        
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
    losing_board = 0
    completed_list = []
    completed_boards = []
    for draw in draw_list:
        this_draw = Number_Draw(draw)
        this_draw.mark_all_numbers(board_list)
        for num in range(len(board_list)):
            if (num in start_points) and (num not in completed_list):
                this_board = Board(board_list[num:num+5])
                if this_board.count_marked()[2] == True:
                    completed_boards.append([num, draw])
                    completed_list.append(num)
        if len(completed_boards) == len(start_points):
            break
    losing_board = completed_boards[-1][0]
    losing_num = completed_boards[-1][1]
    new_board = Board(board_list[losing_board:losing_board+5])
    losing_score = new_board.sum_values()[1] * int(losing_num)
    return {"board start": losing_board, "score": losing_score}

init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_4.txt")
test_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2021\Day_4_test.txt")
draw_order = init_list[0].split(",")
boards = [item.split() for item in init_list[2:]]

#answer to part 1
winning_score = get_winning_board(draw_order, boards)
print(winning_score)

#answer to part 2
losing_score = get_losing_board(draw_order, boards)
print(losing_score)