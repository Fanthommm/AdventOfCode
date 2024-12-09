import sys
import time
import argparse

def part_one(data):
    return 0

def part_two(data):
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Setup for advent of code 2024!')
    parser.add_argument("--input", type=str, default="input.txt", help="Input file")

    args = parser.parse_args()
    input_file = args.input

    with open(input_file) as f:
        lines = f.readlines()
    
    data = [line.rstrip() for line in lines]
    part_one(data)
    starttime = time.time()
    part_two(data)
    endtime = time.time()
    print(f"Execution time: {endtime-starttime}")