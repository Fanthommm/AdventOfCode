def parseData(data):
    result = []
    for line in data:
        numbers = line.split(": ")[1].split(" | ")
        winning = [i for i in numbers[0].split(" ") if i]
        scratch= [i for i in numbers[1].rstrip().split(" ") if i]
        result.append([scratch, winning])
    # print(result)
    return result

def partOne(data):
    gameId=0
    total=0
    for game in data:
        gameId+=1
        gamePoints = 0
        winning = game[0]
        scratch= game[1]

        for number in scratch:
            if number in winning:
                if gamePoints == 0:
                    gamePoints = 1
                else:
                    gamePoints *= 2
        print(f"Game {gameId} : {gamePoints}")
        total += gamePoints
    print(f"TOTAL_ONE = {total}")

def partTwo(data):
    gameId=0
    total=len(data)
    waitingList = list(zip(range(1,len(data)+1), data))
    for line in waitingList:
        # print(f"queue : {len(waitingList)}")
        gameId = line[0]
        # print(gameId)
        gameVal = line[1]
        gamePoints = 0
        winning = gameVal[0]
        scratch= gameVal[1]
        for number in scratch:
            if number in winning:
                gamePoints +=1
        # print(f"Game {gameId} : {gamePoints}")
        for i in range(1,gamePoints+1):
            # if gameId+i <= len(data):
                # print(f"appending {gameId + i}")
                waitingList.append((gameId + i,data[gameId+i-1]))
        total += gamePoints
    print(f"PART_TWO : TOTAL = {total}")



def main():
    with open('input.txt') as f:
        lines = f.readlines()

    parsed = parseData(lines)

    #Part One
    partOne(parsed)

    #PartTwo
    partTwo(parsed)


main()