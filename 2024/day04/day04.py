import argparse
import numpy as np
import time

def is_word_valid(word):
    word = word.tolist()
    return word == list('XMAS') or word == list('SAMX')

def part_one(data):
    matrice = np.asarray([np.asarray(list(d)) for d in data])
    X,Y = matrice.shape
    total_result = 0
    for x in range(X):
        for y in range(Y):
            # HORIZONTAL
            if is_word_valid(matrice[x,y:y+4]):
                # print(matrice[x,y:y+4])
                total_result += 1
            # VERTICAL
            if is_word_valid(matrice[x:x+4,y]):
                # print(matrice[x:x+4,y])
                # print(x,x+4,y)
                total_result += 1
            # DIAGONAL
            if x+4 <= X and y+4 <= Y and is_word_valid(np.array([matrice[x+i,y+i] for i in range(4)])):
                # print([(x+i,y+i) for i in range(4)])
                # print(np.array([matrice[x+i,y+i] for i in range(4)]))
                total_result += 1
        # DIAGONAL INVERSE
        for y in range(Y-1,-1,-1):
            if x+4 <= X and y-3 >= 0 and is_word_valid(np.array([matrice[x+i,y-i] for i in range(4)])):
                # print([(x+i,y-i) for i in range(4)])
                # print(np.array([matrice[x+i,y-i] for i in range(4)]))
                total_result += 1
    # for x in range(X-1,-1,-1):

    print(f"Part one: {total_result}")

def is_mas_or_sam(diag):
    diag = diag.tolist()
    return diag == list('MAS') or diag == list('SAM')

def square_is_valid(square):
    diag1 = square.diagonal()
    diag2 = np.fliplr(square).diagonal()
    return is_mas_or_sam(diag1) and is_mas_or_sam(diag2)


def part_two(data):
    matrice = np.asarray([np.asarray(list(d)) for d in data])
    X,Y = matrice.shape
    total_result = 0
    for x in range(X-2):
        for y in range(Y-2):
            square = matrice[x:x+3,y:y+3]
            if square_is_valid(square):
                total_result += 1
    print(f"Part two: {total_result}")

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