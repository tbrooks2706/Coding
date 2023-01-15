#THE PROBLEM
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
#for the rest you have to use logic based on which segments appear in which letters
    #len 5: 2, 3, 5, len 6: 6, 9, 0

class Letter:
    def __init__(self, input_list, letter) -> None:
        self.letter = letter
        self.patterns = input_list
        self.in_patterns = self.check_in_numbers()
    
    def check_in_numbers(self):
        count = 0
        for string in self.patterns:
            if self.letter in string:
                count += 1
        return count

class SignalPattern:
    def __init__(self, string, numbers_dict) -> None:
        self.string = string
        self.lookup = numbers_dict
        self.len_dict = {2: 1, 3: 7, 4: 4, 7: 8}
        self.len = len(string)
        self.digit = self.return_number()
        self.is_unique = self.digit in [1, 4, 7, 8]
    
    def return_number(self):
        #initial lookup based on len for 1478 - these need to be identifiable independent of self.lookup because they are the basis for it
        if self.len in self.len_dict.keys():
            return self.len_dict[self.len]
        #lookup the rest from logic-based dictionary
        for key, value in self.lookup.items():
            if sorted(self.string) == sorted(value):
                return key

class Display:
    def __init__(self, input_list) -> None:
        self.full_list = input_list
        self.output_codes = input_list[11:15]
        self.patterns_list = input_list[:10]
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
        self.numbers = {2: self.two, 3: self.three, 5: self.five, 0: self.zero, 9: self.nine, 6: self.six}
        self.assign_rest()
        self.unique_occurrences = self.count_unique_occurrences()
        self.output_digits_string = self.find_output_digits()[1]
    
    def count_unique_occurrences(self):
        count = 0
        for string in self.output_codes:
            this_pattern = SignalPattern(string, self.digits)
            if this_pattern.is_unique == True:
                count += 1
        return count
    
    def find_output_digits(self):
        digit_list = []
        digit_string = ""
        for string in self.output_codes:
            this_pattern = SignalPattern(string, self.digits)
            digit_list.append(this_pattern.digit)
            digit_string += str(this_pattern.digit)
        return [digit_list, digit_string]
    
    def assign_initial(self):
        #assign 1478 to strings in digits dict
        for string in self.patterns_list:
            this_pattern = SignalPattern(string, self.digits)
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
            #middle (in 7 patterns) = is in the number 4 (only middle and bottom are left, and bottom isn't in 4)
            elif letter in self.digits[4]:
                self.positions["middle"] = letter
            #bottom (in 7 patterns) = else
            else:
                self.positions["bottom"] = letter
    
    def assign_rest(self):
        #go through every string
        for string in self.patterns_list:
            #check the string against the letters for every number
            for key, value in self.numbers.items():
                if string not in self.digits.values():
                    letter_match = True
                    for letter in string:
                        if letter not in value:
                            letter_match = False
                            break
                    #if full match, assign string to number in dictionary and move on to next string
                    #if not full match, check against the next number
                    if letter_match == True:
                        self.digits[key] = string
                        break

def count_all_unique(input_list):
    count = 0
    for display in input_list:
        this_display = Display(display)
        count += this_display.count_unique_occurrences()
    return count

def sum_all_outputs(input_list):
    sum = 0
    for display in input_list:
        this_display = Display(display)
        sum += int(this_display.output_digits_string)
    return sum

with open(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2021\Day_8.txt") as nickname:
    working_list = [line.split() for line in nickname]     

#part 1: how many times do 1,4,7,8 (the easy ones) occur in the output values?
#answer part 1
unique_count = count_all_unique(working_list)
print(unique_count)

#part 2: what is the sum of all output codes
#answer part 2
output_sum = sum_all_outputs(working_list)
print(output_sum)