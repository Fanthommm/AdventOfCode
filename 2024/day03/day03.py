import re

def multiply(string):
    #Get the result of the mult operation
    regex2 = r"\d{1,3}"

    numbers = re.findall(regex2, string)
    return int(numbers[0]) * int(numbers[1])

def part_one(data):
    regex = r"mul\(\d{1,3},\d{1,3}\)"

    total = 0
    for line in data:
        goods = re.findall(regex, line)
        for good in goods:
            total += multiply(good)
    print(f"Part one : {total}")

def part_two(data):
    regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

    total = 0
    do = True #Enables the multiplication
    for line in data:
        goods = re.findall(regex, line)
        for good in goods:
            if good == "do()":
                print(good)
                do = True
            elif good == "don't()":
                print(good)
                do = False
            elif do:
                print(good)
                total += multiply(good)
    
    print(f"Part two : {total}")


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    
    data = [line.rstrip() for line in lines]
    # part_one(data)
    part_two(data)