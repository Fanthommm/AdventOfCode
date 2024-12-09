import argparse

def is_increasing(line):
    if line == sorted(line):
        return True
    
def is_decreasing(line):
    if line == sorted(line, reverse=True):
        return True
    
def check_step(line):
    tmp = line[0]
    for i in line[1:]:
        if abs(tmp - i) > 3 or abs(tmp - i) < 1 :
            return False
        tmp = i
    return True

def part_one(data):
    result = 0
    for line in data:
        line = [int(num) for num in line.split(" ")]
        if is_increasing(line) or is_decreasing(line):
            check = check_step(line)
        else:
            check = False
        if check:
            print(line)
            result += 1
    print("part one :" + str(result))

def is_valid(line):
    if is_increasing(line) or is_decreasing(line):
        return check_step(line)
    else:
        return False

def part_two(data):
    result = 0
    for line in data:
        line = [int(num) for num in line.split(" ")]
        if not is_valid(line):
            saved = False
            for i in range(len(line)):
                trunc = line.copy()
                trunc.pop(i)
                if is_valid(trunc):
                    saved = True
            if saved:
                result += 1
        else:
            result += 1
    print("part two :" + str(result))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Setup for advent of code 2024!')
    parser.add_argument("--input", type=str, default="input.txt", help="Input file")

    args = parser.parse_args()
    input_file = args.input

    with open(input_file) as f:
        lines = f.readlines()
    
    data = [line.rstrip() for line in lines]
    part_one(data)
    part_two(data)