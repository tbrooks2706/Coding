#recreate wordle
#the rules
#aim is to correctly guess the target word within 6 guesses
#input is a 5 character string, of only letters A-Z, not case sensitive
    #input validation

import copy

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def create_alphabet_dict():
    dct = {}
    for letter in alphabet:
        dct[letter] = 0
    return dct

def count_letters(word, dictionary):
    for position in word:
        dictionary[position] += 1

class Target:
    def __init__(self, word) -> None:
        self.word = word.upper()
        self.letter_count = create_alphabet_dict()
        count_letters(self.word, self.letter_count)

class Guess:
    def __init__(self, word, target) -> None:
        self.guess_word = word.upper()
        self.target_word = target.upper()
        self.default_mark = "B"
        self.correct_mark = "G"
        self.diff_mark = "Y"
        self.letter_count = create_alphabet_dict()
        self.green_count = create_alphabet_dict()
        self.yellow_count = create_alphabet_dict()
        count_letters(self.guess_word, self.letter_count)
        self.marks = [
            [self.guess_word[0], self.default_mark], 
            [self.guess_word[1], self.default_mark], 
            [self.guess_word[2], self.default_mark], 
            [self.guess_word[3], self.default_mark], 
            [self.guess_word[4], self.default_mark]
            ]
        self.mark_green()
        self.max_yellow_count = self.calc_max_yellows()
        self.mark_yellow()
        self.result = self.marks[0][1]+self.marks[1][1]+self.marks[2][1]+self.marks[3][1]+self.marks[4][1]

    def print_out(self):
        print("Target:", self.target_word)
        print("Guess: ", self.guess_word)
        print("Result:", self.result)

    def mark_green(self):
        ind = 0
        for position in self.marks:
            if position[0] == self.target_word[ind]:
                position[1] = self.correct_mark
                self.green_count[position[0]] += 1
            ind += 1

    #number of occs in the target word, minus number of greens
    def calc_max_yellows(self):
        max_yellow_count = copy.deepcopy(self.letter_count)
        for letter in max_yellow_count:
            target_count = example_target.letter_count[letter]
            greens = self.green_count[letter]
            max_yellows = max(target_count - greens, 0)
            max_yellow_count[letter] = max_yellows
        return max_yellow_count
    
    #for each position in guess word, mark yellows up to the maximum number
    def mark_yellow(self):
        ind = 0
        for position in self.marks:
            if position[0] not in self.target_word:
                continue
            if position[1] == self.correct_mark:
                continue
            else:
                max_yellows = self.max_yellow_count[position[0]]
                current_yellows = self.yellow_count[position[0]]
                if current_yellows < max_yellows:
                    position[1] = self.diff_mark
                    self.yellow_count[position[0]] += 1
                

example_target = Target("STERN")
#print("target:",example_target.letter_count)
example_guess = Guess("STARE", example_target.word)
print(example_guess.print_out())
#print("yellows:",example_guess.max_yellow_count)