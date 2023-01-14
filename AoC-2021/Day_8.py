import general_functions

#multiple four digit displays
#each display is made up of digits
#each digit is made up of 7 segments, turned off or on to produce a visual digit
#wires are connected to segments randomly
#connection scramble is different for each display, but consistent between the digits WITHIN each display

#each line in file is a display
    #all 10 unique patterns
    #1 four digit output value
    #each string of the 10 is one scrambled digit
#you can work out which digit is which for SOME just by looking at the length of the string
    #1=2, 2=5, 3=5, 4=4, 5=5, 6=6, 7=3, 8=7, 9=6, 0=6
    #len 2: 1, len 3: 7, len 4: 4, len 7: 8
    #len 5: 2, 3, 5, len 6: 6, 9, 0

#part 1: how many times do 1,4,7,8 (the easy ones) occur in the output values?

#part 2
#you can work out what the pattern looks like by analysing the result of those four numbers
#in this order:
    #bottom left (in 4 patterns) = only letter in exactly 4 patterns
    #bottom right (in 9 patterns, all except 2) = only letter in exactly 9 patterns
    #top right (in 8 patterns) = in 1, and is not bottom right
    #top (in 8 patterns) = in 7 and 8, not in 1 or 4
    #top left (in 6 patterns) = in 8 and 4, not in 1 or 7
    #bottom (in 7 patterns) = is in exactly 7 patterns, and only in one of 1478
    #middle (in 7 patterns) = is in exactly 7 patterns, and in >1 one of 1478

with open(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_8_test.txt") as nickname:
    working_list = [line.split() for line in nickname]     
#print(working_list)

part2_example = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf".split()
print(part2_example)

class Letter:
    def __init__(self, input_list, letter) -> None:
        self.letter = letter
        self.patterns = input_list
        # self.in_1 = False
        # self.in_4 = False
        # self.in_7 = False
        # self.in_8 = False
        self.in_patterns = self.check_in_numbers()
        self.in_unique_patterns = 0
    
    def check_in_numbers(self):
        count = 0
        for string in self.patterns:
            if self.letter in string:
                count += 1
        return count

example_letter = Letter(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'], "e")
print(example_letter.in_patterns)

class SignalPattern:
    def __init__(self, string) -> None:
        self.string = string
        self.len = len(string)
        self.digit = self.return_number()
        self.is_unique = self.digit in [1, 4, 7, 8]
    
    def return_number(self):
        if self.len == 2:
            return 1
        elif self.len == 3:
            return 7
        elif self.len == 4:
            return 4
        elif self.len == 7:
            return 8
        else:
            return "Unknown"

example_pattern = SignalPattern("abcd")
#print(example_pattern.is_unique)

class Display:
    def __init__(self, input_list) -> None:
        self.full_list = input_list
        self.output_codes = input_list[11:15]
        self.patterns_list = input_list[:10]
        self.unique_occurrences = self.count_unique_occurrences()
        self.output_digits_list = self.find_output_digits()[0]
        self.output_digits_string = self.find_output_digits()[1]
        self.letters = "abcdefg"
        self.positions = {"top": "", "topleft": "", "topright": "", "middle": "", "bottomleft": "", "bottomright": "", "bottom": ""}
        self.digits = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
        self.assign_initial()
        self.two = [self.positions["top"], self.positions["topright"], self.positions["middle"], self.positions["bottomleft"], self.positions["bottom"]]
        self.three = [self.positions["top"], self.positions["topright"], self.positions["middle"], self.positions["bottomright"], self.positions["bottom"]]
        self.five = [self.positions["top"], self.positions["topleft"], self.positions["middle"], self.positions["bottomright"], self.positions["bottom"]]
        self.zero = [self.positions["top"], self.positions["topright"], self.positions["topleft"], self.positions["bottomright"], self.positions["bottomleft"], self.positions["bottom"]]
        self.nine = [self.positions["top"], self.positions["topleft"], self.positions["middle"], self.positions["bottomright"], self.positions["topright"], self.positions["bottom"]]
        self.six = [self.positions["top"], self.positions["topleft"], self.positions["middle"], self.positions["bottomright"], self.positions["bottomleft"], self.positions["bottom"]]
        self.assign_rest()
    
    def count_unique_occurrences(self):
        count = 0
        for string in self.output_codes:
            this_pattern = SignalPattern(string)
            if this_pattern.is_unique == True:
                count += 1
        return count
    
    def find_output_digits(self):
        digit_list = []
        digit_string = ""
        for string in self.output_codes:
            this_pattern = SignalPattern(string)
            digit_list.append(this_pattern.digit)
            digit_string += str(this_pattern.digit)
        return [digit_list, digit_string]
    
    def assign_initial(self):
        #assign 1478 to strings in digits dict
        for string in self.patterns_list:
            this_pattern = SignalPattern(string)
            if this_pattern.is_unique == True:
                self.digits[this_pattern.digit] = string
        for letter in self.letters:
            this_letter = Letter(self.patterns_list, letter)
            #bottom left (in 4 patterns) = only letter in exactly 4 patterns
            #bottom right (in 9 patterns, all except 2) = only letter in exactly 9 patterns
            #top left (in 6 patterns) = only letter in exactly 6 patterns
            if this_letter.in_patterns == 4:
                self.positions["bottomleft"] = letter
            elif this_letter.in_patterns == 9:
                self.positions["bottomright"] = letter
            elif this_letter.in_patterns == 6:
                self.positions["topleft"] = letter            
            #top right (in 8 patterns) = in 1, and is not bottom right
            elif letter in self.digits[1]:
                self.positions["topright"] = letter
            #top (in 8 patterns) = in 7 and 8, not in 1 or 4
            elif (letter in self.digits[7]) and (letter in self.digits[8]) and (letter not in self.digits[1]) and (letter not in self.digits[4]):
                self.positions["top"] = letter
            #middle (in 7 patterns) = is in 4 (only middle and bottom are left, and bottom isn't in 4)
            elif letter in self.digits[4]:
                self.positions["middle"] = letter
            #bottom (in 7 patterns) = else
            else:
                self.positions["bottom"] = letter
    
    def assign_rest(self):
        pass
    #######################################assign numbers into dictionary based on position specs in init############################################



        

example_display = Display(part2_example)
print(example_display.patterns_list)
print(example_display.digits)
print(example_display.positions)
#print(example_display.two)
def count_all_unique(input_list):
    count = 0
    for display in input_list:
        this_display = Display(display)
        count += this_display.unique_occurrences
    return count

#answer part 1
unique_count = count_all_unique(working_list)
#print(unique_count)

#answer part 2




