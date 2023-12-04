digits = ['0','1','2','3','4','5','6','7','8','9']

def around(data, position):
    # Take position and append everyneighbour in a list
    # Indexes :
    # 0 1 2
    # 3 4 5
    # 6 7 8
    i = position[0]
    j = position[1]
    neighbors = []
    for jx in [j-1,j,j+1]:
        for ix in [i-1,i,i+1]:
            if jx >= 0 and jx < len(data) and ix >=0 and ix < len(data[j])-1:
                neighbors.append(data[jx][ix])
            else:
                neighbors.append(None)

    return neighbors

def textToMat(text):
    matrix = []
    for i in range(len(text)):
        line = text[i]

def inspect(data, position):
    result = ["",1,False]
    neighbors = around(data, position)
    if neighbors[4] in digits:
        result[0] = neighbors[4]
        for i in neighbors:
            if i!= '.' and i not in digits and i != None:
                result[2] = True
        if neighbors[5] in digits:
            rec = inspect(data, (position[0]+1,position[1]))
            result[0] += rec[0]
            result[1] += (rec[1])
            result[2] = result[2] or rec[2]
    return result

def partOne(lines):
    #print(around(lines, (4,1)))
    valid = []
    for idLine in range(len(lines)):
        line = lines[idLine]
        idCharac = 0
        while idCharac <= (len(line)):
            result = inspect(lines, (idCharac, idLine))
            idCharac += result[1]
            if result[2] :
                valid.append(int(result[0]))
    
    print(f"Sum of part numbers : {sum(valid)}")

def inspect2(data, position):
    result = ["",1,None]
    neighbors = around(data, position)
    if neighbors[4] in digits:
        result[0] = neighbors[4]
        for i in range(len(neighbors)):
            charac = neighbors[i]
            if charac== '*':
                    result[2] = (position[0]+(int(i)%3 - 1),position[1]+(int(i)//3 - 1))
        if neighbors[5] in digits:
            rec = inspect2(data, (position[0]+1,position[1]))
            result[0] += rec[0]
            result[1] += (rec[1])
            result[2] = result[2] or rec[2]
    return result

def calculateSumGR(data):
    total = 0
    while data != []:
        valid1 = data.pop()
        print(valid1)
        gearRatio = 0
        for i in range(len(data)):
            if data[i][2] == valid1[2]:
                print(f">> {data[i]}")
                gearRatio = int(valid1[0]) * int(data[i][0])
        total += gearRatio
    return total




# list.remove(id)

def partTwo(lines):
    gearRatios = []
    #print(around(lines, (4,1)))
    valid = []
    for idLine in range(len(lines)):
        line = lines[idLine]
        idCharac = 0
        while idCharac <= (len(line)):
            result = inspect2(lines, (idCharac, idLine))
            idCharac += result[1]
            if result[2] :
                valid.append(result)
            
    total = calculateSumGR(valid)

    print(f"Sum of gear ratios : {total}")



def main():
    with open('input.txt') as f:
        lines = f.readlines()

    #Part One
    partOne(lines)

    #PartTwo
    partTwo(lines)


main()