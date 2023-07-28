#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

string = input("Enter a string: ")
is_palindrome = string == string[::-1]
print(string, "Palindrome:", is_palindrome)