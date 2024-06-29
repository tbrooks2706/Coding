#recreate wordle
#the rules
#aim is to correctly guess the target word within 6 guesses
#input is a 5 character string, of only letters A-Z, not case sensitive
    #input validation

import unittest

class SomeTests(unittest.TestCase):
    #guessing STENT when the target is SPEAK
    def test_wordle_a(self):
        self.assertEqual("STENT", """ You guessed STENT.
    S Green
    T Black
    E Green
    N Black
    T Black
    5 guesses left.""")
    
    def setUp(self):
        pass

    def tearDown(self) -> None:
        return super().tearDown()

#unittest.main()

