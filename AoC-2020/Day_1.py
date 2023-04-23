import copy

#main function used in both parts
def find_two(input_list, target_total):
    new_list = []
    ind = 0
    for num in input_list:
        target = target_total - num
        to_search = copy.deepcopy(input_list)
        to_search.pop(ind)
        ind += 1
        if target in to_search:
            new_list = [num, target]
            break
    return new_list

#used in part 2 only
def find_three(input_list, target_total):
    new_list = []
    ind = 0
    for num in input_list:
        target = target_total - num
        to_search = copy.deepcopy(input_list)
        to_search.pop(ind)
        ind += 1
        other_two = find_two(to_search, target)
        if other_two != []:
            new_list = [num, other_two[0], other_two[1]]
            break
    return new_list

with open(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Coding\AoC-2020\Day_1.txt") as file:
    working_list = [int(line) for line in file]
    working_list.sort(reverse=True)

numbers_part_1 = find_two(working_list, 2020)
answer_part_1 = numbers_part_1[0] * numbers_part_1[1]
print(answer_part_1)

numbers_part_2 = find_three(working_list, 2020)
answer_part_2 = numbers_part_2[0] * numbers_part_2[1] * numbers_part_2[2]
print(answer_part_2)


