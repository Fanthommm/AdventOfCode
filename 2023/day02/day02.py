def sparseValue(lines):
    sparsed =[]
    for id in range(len(lines)):
            #Get game ID
            game = lines[id]
            id +=1

            #Remove \n
            game = game.rstrip()

            #Get content of the game
            game = game.split(": ")[1]
            sets = game.split("; ")
            data = []
            for set in sets :
                set = set.split(", ")
                newSet = {}
                for couple in set:
                    couple = couple.split(" ")
                    newSet[couple[1]]=couple[0]
                data.append(newSet)
            sparsed.append(data)

    return sparsed

def partOne(data):

    max = {'red' : 12, 'green' : 13, 'blue' : 14}

    total = 0

    for id in range(len(data)):
            gameIsValid = True

            #Get game ID
            game = data[id]
            id +=1

            for set in game :
                for color in set:
                    if int(set[color]) > max[color]:
                        gameIsValid = False

            
            print(f"===Game {id}===")
            print(data)
            print(f"IsValid : {gameIsValid}")

            if gameIsValid:
                total += id

    print(f"TOTAL = {total}")  

def calculatePower(fewest):
    power = 1
    for color in fewest:
        power *= int(fewest[color])
    print(f"Power : {power}")    
    return power

def partTwo(data):
    total = 0

    for id in range(len(data)):
            #Get game ID
            game = data[id]
            print(f"===Game n°{id}===")
            print(game)
            id +=1

            # Initialise fewest
            fewest = {'red' : None, 'green' : None, 'blue' : None}

            # We collect minimum necessaries value for fewest numbers
            for set in game :
                for color in fewest:
                    if color in set:
                        if fewest[color] is None or int(fewest[color]) < int(set[color]):
                            fewest[color] = set[color]
            print(f"Fewest cubes : {fewest}")

            # Calculate power
            power = calculatePower(fewest)

            # Add to total
            total += power

    print(total)

            

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    sparsed = sparseValue(lines)
    # print(sparsed)

    #===PART ONE===
    # partOne(sparsed)

    #===PART TWO===
    partTwo(sparsed)


main()