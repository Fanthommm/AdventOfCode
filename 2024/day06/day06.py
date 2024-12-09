import time
import sys
import numpy as np

# Orientation :
# 0 : N
# 1 : E
# 2 : S
# 3 : W

# Codes
# 0 : .
# 1 : #


def part_one(data):
    player = set_starting_position(data)
    max_x, max_y = data.shape

    visited_position = []
    while (
        player[0] >= 0 and player[0] < max_x and
        player[1] >= 0 and player[1] < max_y
    ):
        visual_map[player[0], player[1]] = 2
        # print(visual_map)
        visited_position.append((player[0], player[1]))
        player = move(data, player, max_x, max_y)
    
    print(f"Part one : {len(set(visited_position))}")

    return visited_position
# def resolve_labyrinth(data):


def part_two(data, visited):
    start = set_starting_position(data)
    max_x, max_y = data.shape

    obstacles = []
    for (i,j) in visited:
        if data[i,j] == 0:
            data[i,j] = 1

            player = start

            max_x, max_y = data.shape

            visited_position = []
            check_iter = 0
            while (
                player[0] >= 0 and player[0] < max_x and
                player[1] >= 0 and player[1] < max_y
            ):
                # print(visual_map)
                visited_position.append(player)
                # print(visited_position)
                player = move(data, player, max_x, max_y)

                check_iter += 1

                if player in visited_position:
                    obstacles.append((i,j))
                    print(i,j)
                    break

                if check_iter > 10000:
                    raise Exception("Infinite loop")

            data[i,j] = 0
        else:
            pass
    
    print(f"Part two : {len(set(obstacles))}")

def set_starting_position(data : np.array):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i,j] == 2:
                data[i,j] = 0
                return (i,j,0)
    return None

def find_next_step(player):
    x,y,orientation = player

    if orientation == 0:
        x -= 1
    elif orientation == 1:
        y += 1
    elif orientation == 2:
        x += 1
    elif orientation == 3:
        y -= 1

    return x,y

def move(map, player, max_x, max_y):
    x,y,orientation = player

    next_x, next_y = find_next_step(player)
    if (
        next_x < 0 or next_x >= max_x or
        next_y < 0 or next_y >= max_y
    ):
        x = next_x
        y = next_y
    elif map[next_x, next_y] == 1:
        orientation = (orientation + 1) % 4
    else:
        x = next_x
        y = next_y
    
    return x,y,orientation

if __name__ == "__main__":
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        lines = f.readlines()

    np.set_printoptions(threshold=sys.maxsize)
    
    data = np.array([[0 if char == '.' else (1 if char == '#' else 2) for char in line.rstrip()] for line in lines])
    visual_map = data.copy()

    # matrice = np.asarray([np.asarray(list(d)) for d in data])

    visited = part_one(data.copy())
    starttime = time.time()
    part_two(data, list(set(visited)))
    endtime = time.time()
    print(f"Execution time: {endtime-starttime}")