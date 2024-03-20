#coding kata

def pig_latin(word):
    if len(word) < 4:
        return word
    return word[1:]+word[0]+"ay"

def josephus(items,k):
    #your code here
    result_arr = []
    result_arr.append(items.pop(k-1))
    return result_arr