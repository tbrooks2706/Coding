#https://adventofcode.com/2021/day/10

#puzzle input is navigation subsystem
#lines contain chunks
#chunks must open and close with a matching pair of characters - (), [], {}, <>
#chunks don't have to be separated by any delimiter character
#chunks can contain other chunks - eg. [<>({}){}[([])<>]] is a valid chunk which contains multiple nested

#in puzzle input, all lines are either incomplete or corrupted
#corrupted = any chunk within the line opens/closes without a matching pair of 4 above
    #there has to be an invalid closing character within the line
    #just having pairs that aren't closed does not count as corrupted
#stop at the first invalid closing character
    #[<(<(<(<{}))><([]([]() is corrupted - first character is char 11, first )
#count how many invalid closing characters are found, and multiply them by the scores
#) = 3, ] = 5, } = 1197, > = 25197
#sum the scores for each corrupted line in the input file - "syntax error score"

with open(r"c:/Users/Tom.Brooks/OneDrive - BJSS Ltd/Documents/Coding/Coding/AoC-2021\Day_10_test.txt") as input_file:
    init_list = []
    for row in input_file:
        init_list.append(row.replace("\n",""))
print(init_list)

#could use subclasses? Line, CorruptedLine (Line), IncompleteLine (Line)
#have a "latest incomplete char" line then loop through line
#store first invalid char as an instance variable within CorruptedLine?
#represent characters to check as a dictionary?
check_dict = {"<": ">", "[": "]", "{": "}", "(": ")"}
reverse_dict = {">": "<", "]": "[", "}": "{", ")": "("}
#print(check_dict.keys())

class Line:
    def __init__(self, string) -> None:
        self.string = string
        self.len = len(string)
        self.is_corrupted = False
        self.first_invalid = ""
        self.check_corrupted()

    def check_corrupted(self):
        open_char = ""
        match_char = ""
        ind = 0
        for char in self.string:
            #if open character
            if char in check_dict.keys():
                open_char = char
            #if closed character
            else:
                match_char = check_dict.get(open_char)
                #if it matches the last open character, look back to the previous open character and set open_char to that, then move to next char
                ############change it - previous UNRESOLVED open character#####################
                if char == match_char:
                    for revchar in reversed(self.string[:ind]):
                        if revchar in check_dict.keys():
                            open_char = revchar
                            break
                #if closed and it doesn't match open_char, set is_corrupted and first_invalid and break loop
                else:
                    self.is_corrupted = True
                    self.first_invalid = char
                    break
            ind += 1
            

example_line = Line("[({(<(())[]>[[{[]{<()<>>")
print(example_line.first_invalid)
print(example_line.is_corrupted)



# string = "pythonic"
# ind = 0
# for char in reversed(string):
#     print(char)