import math
import time
import argparse
from itertools import combinations
import sympy as sp

def trouve_droite(p1, p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - m * p1[0]
    return m, b

def distance(p1, p2):
    return sp.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def find_antinode(p1, p2, shape):
    x, y = sp.symbols('x y', integer=True)
    m, b = trouve_droite(p1, p2)

    # Define equations
    eq1 = sp.Eq(y, m * x + b)
    eq2 = sp.Eq(distance(p1, (x, y)), 2 * distance(p2, (x, y)))
    # eq3 = sp.Eq(2 * distance(p1, (x, y)), distance(p2, (x, y)))

    # Define constraints
    x_constraint = sp.And(x >= 0, x <= shape[0])
    y_constraint = sp.And(y >= 0, y <= shape[1])

    # Solve the equations
    solutions = sp.nonlinsolve([eq1, eq2], [x, y])
    
    # Apply constraints manually
    constrained_solutions = [
        sol for sol in solutions
        if x_constraint.subs({x: sol[0], y: sol[1]}) and y_constraint.subs({x: sol[0], y: sol[1]})
    ]

    return constrained_solutions

def part_one(data):
    antennas = {}
    shape = (len(data), len(data[0]))
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] != ".":
                if data[x][y] in antennas.keys():
                    antennas[data[x][y]].append((x,y))
                else:
                    antennas[data[x][y]] = [(x,y)]
    
    for type in antennas.keys():
        list_type = antennas[type]
        print(f"Type: {type}")
        for pair in combinations(list_type, 2):
            antidones = find_antinode(pair[0], pair[1], shape)
            print(antidones)
            # print((2.0).is_integer())
            print([antidone for antidone in antidones if float(antidone[0]).is_integer() and float(antidone[1]).is_integer()])


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

    starttime = time.time()
    part_one(data)
    part_two(data)
    endtime = time.time()
    print(f"Execution time: {endtime-starttime}")