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

def check_step_two(line):
    tmp = line[0]
    lives = 1
    for i in line[1:]:
        if abs(tmp - i) > 3 or abs(tmp - i) < 1 :
            lives -= 1
        tmp = i
    if lives < 0:
        return False
    else:
        return True

def part_two(data):
    result = 0
    for line in data:
        line = [int(num) for num in line.split(" ")]
        if is_increasing(line) or is_decreasing(line):
            check = check_step_two(line)
        else:
            check = False
        if check:
            print(line)
            result += 1
    print("part two :" + str(result))



if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    
    data = [line.rstrip() for line in lines]
    part_one(data)
    part_two(data)