import argparse
import time


def calculate(numbers):
    operations = [int(numbers[0])]
    for i in range(1, len(numbers)):
        new_operation = []
        for operation in operations:
            new_operation.append(operation + int(numbers[i]))
            new_operation.append(operation * int(numbers[i]))
        operations = new_operation

    return operations


def part_one(data):
    total_result = 0
    for line in data:
        line = line.split(":")
        test_value = line[0]
        numbers = line[1].split(" ")[1:]
        possibilities = calculate(numbers)
        for possibility in possibilities:
            if possibility == int(test_value):
                total_result += int(test_value)
                break
    print(f"Part one: {total_result}")


def calculate_two(numbers):
    operations = [int(numbers[0])]
    for i in range(1, len(numbers)):
        new_operation = []
        for operation in operations:
            new_operation.append(operation + int(numbers[i]))
            new_operation.append(operation * int(numbers[i]))
            new_operation.append(int(str(operation) + str(int(numbers[i]))))
        operations = new_operation

    return operations


def part_two(data):
    total_result = 0
    for line in data:
        line = line.split(":")
        test_value = line[0]
        numbers = line[1].split(" ")[1:]
        possibilities = calculate_two(numbers)
        for possibility in possibilities:
            if possibility == int(test_value):
                total_result += int(test_value)
                break
    print(f"Part two: {total_result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Setup for advent of code 2024!')
    parser.add_argument("--input", type=str, default="input.txt", help="Input file")

    args = parser.parse_args()
    input_file = args.input

    with open(input_file) as f:
        lines = f.readlines()

    data = [line.rstrip() for line in lines]

    starttime = time.time()
    part_one(data)
    part_two(data)
    endtime = time.time()
    print(f"Execution time: {endtime-starttime}")
