#https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def ask_user():
    length = int(input("How many Fibonacci numbers do you want me to generate? (>1) "))
    generate_sequence(length)

def generate_sequence(seq_length):
    seq = [0, 1]
    for x in range(2, seq_length):
        #print(x)
        seq.append(seq[x-1] + seq[x-2])
    print(seq)

ask_user()