import sys
from ..utils import Input

def process_input(lines):
    list1 = []
    list2 = []
    for line in lines:
        line = line.split("\n")[0].split("   ")
        list1.append(line[0])
        list2.append(line[1])
    return list1, list2       

def part_one(list1, list2):
    list1.sort()
    list2.sort()

    if len(list1) != len(list2):
        print("Error: lists are not the same length")
        return
    else:
        total_sum = 0
        for i in range(len(list1)):
            total_sum += abs(int(list1[i]) - int(list2[i]))

    print(f"TOTAL = {total_sum}")

def part_two(list1, list2):
    # for i in list1:
    #     if i in list2:
    #         print(list2.index(i))
    total_result = 0
    for i in list1:
        tmp = 0
        while i in list2:
            tmp += 1
            list2.remove(i)
        total_result += tmp*int(i)
    print(f"TOTAL = {total_result}")

def main():
    with open('day01/input.txt') as f:
        lines = f.readlines()
    
    list1, list2 = process_input(lines)

    part_one(list1, list2)
    part_two(list1, list2)

if __name__ == "__main__":
    main()
