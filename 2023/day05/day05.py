def sparseMap(lines):
    map = []
    line = None
    for line in lines:
        if line == '\n' :
            break
        line = line.rstrip()
        split = line.split(" ")
        source = int(split[1])
        destination = int(split[0])
        map.append([source, source+int(split[2]), destination, destination+int(split[2])])
        # for i in range(0,int(split[2])):
        #     source = int(split[1]) + i
        #     destination = int(split[0]) + i
        #     map.append([source, destination])
            # map.append([split[1],split[0],split[2]])
    # sortedList = sorted(map, key=lambda x: int(x[0]))

    # j = 0
    # for i in range(int(sortedList[1][0]), int(sortedList[-1][0])):
    #     # print(i)
    #     isMapped = False
    #     for check in sortedList:
    #         if i == check[0]:
    #             isMapped = True
    #     if not isMapped:
    #         sortedList.append([i, j, 1])
    #     else:
    #         j+=1
            
    return map

def parseData(data):
    for idLine in range(len(data)):
        line = data[idLine]
        # print(line)
        line = line.rstrip()
        if "seeds" in line:
            seeds = line.split(": ")[1].split(" ")
        match line:
            case "seed-to-soil map:":
                seed2soil = sparseMap(data[idLine+1:])

            case "soil-to-fertilizer map:":
                soil2fert = sparseMap(data[idLine+1:])

            case "fertilizer-to-water map:":
                fert2water = sparseMap(data[idLine+1:])

            case "water-to-light map:":
                water2light = sparseMap(data[idLine+1:])

            case "light-to-temperature map:":
                light2temp = sparseMap(data[idLine+1:])
            
            case "temperature-to-humidity map:":
                temp2hum = sparseMap(data[idLine+1:])
            
            case "humidity-to-location map:":
                hum2loc = sparseMap(data[idLine+1:])
            
    return {'seeds':seeds, 'seed2soil':seed2soil, 'soil2fert':soil2fert, 'fert2water':fert2water, 'water2light':water2light, 'light2temp':light2temp, 'temp2hum':temp2hum, 'hum2loc':hum2loc}

def initDict(seeds):
    dict = {}
    for seed in seeds:
        dict[seed] = [seed]
    return dict

# def convert(data, map):
#     for line in data:
#         sourceSeed = data[line][-1]
#         found = False
#         for mapLine in map:
#             sourceDeb = int(mapLine[0])
#             sourceFin = int(mapLine[1])
#             destinationDeb = int(mapLine[2])
#             destinationFin = int(mapLine[3])
#             if sourceSeed in range(sourceDeb, sourceFin):
#                 found = True
#                 if data[source]:
#                     data[source] = data[source].append(destination)
#                 else:
#                     data[source] = destination
#         if not found:
#             data[sourceSeed].append(sourceSeed)
#     return data

def convert(sourceSeed, map):
    result = 0
    found = False
    for mapLine in map:
        sourceDeb = int(mapLine[0])
        sourceFin = int(mapLine[1])
        destinationDeb = int(mapLine[2])
        destinationFin = int(mapLine[3])
        if sourceDeb <= int(sourceSeed) <= sourceFin:
            found = True
            result = destinationDeb + (int(sourceSeed) - sourceDeb)
    if not found:
        result = int(sourceSeed)
    return result

def partOne(parsed):
    for i in parsed:
        if i == 'seeds':
            dico = initDict(parsed['seeds'])
        # elif i == 'seed2soil':
        else:
            for line in dico:
                dico[line].append(convert(dico[line][-1], parsed[i]))
    # result = sorted(dict, key=lambda x: int(dict[x][-1]))
    sorted_dict = dict(sorted(dico.items(), key=lambda item: int(item[1][-1])))
    # print(sorted_dict)
    print(f"Réponse P1 : {list(sorted_dict.values())[0][-1]}")


def initList(seeds):
    dict = []
    while seeds!=[]:
        seed = int(seeds.pop())
        rangeOfSeed = int(seeds.pop())
        dict.append((seed,seed+rangeOfSeed))
    return dict

def valeurs_communnes(fourchette1, fourchette2):
    (a, b) = fourchette1
    (c, d) = fourchette2
    
    if (a <= c <= b) or (a <= d <= b) or (c <= a <= d) or (c <= b <= d):
        # debut = min(a,c)
        debut_commune = max(a, c)
        fin_commune = min(b, d)
        # fin = max(b,d)
        return (debut_commune, fin_commune)
        # return (debut, debut_commune, fin_commune, fin)
    else:
        None
        # return (debut, None, None, fin)

def convert2(sourceSeed, map):
    result = []
    found = False
    queue = []
    seedFinList = []
    queue.append(sourceSeed)
    for mapLine in map:
        queueItem = queue.pop()
        print(queueItem)
        seedDeb = queueItem[0]
        seedFin = queueItem[1]
        sourceDeb = int(mapLine[0])
        sourceFin = int(mapLine[1])
        destinationDeb = int(mapLine[2])
        destinationFin = int(mapLine[3])
        intersection = valeurs_communnes((seedDeb, seedFin), (sourceDeb, sourceFin))
        print(intersection)
        if intersection:
            found = True
            # result.append([intersection[0],intersection[1]-1])
            diff = abs(intersection[0] - seedDeb)

            if seedDeb <= intersection[0] <= seedFin <= intersection[1]:
                print(1)
                if seedDeb != intersection[0]:
                    queue.append((seedDeb,intersection[0]-1))
                result.append((destinationDeb, destinationDeb + diff))
 
            if intersection[0] <= seedDeb <= intersection[1] <= seedFin:
                print(2)
                result.append((destinationDeb, destinationDeb + diff))
                if intersection[1] != seedFin:
                    queue.append((intersection[1]+1,seedFin))

            if seedDeb < intersection[0] <= intersection[1] < seedFin:
                print(3)
                queue.append((seedDeb,intersection[0]-1))
                result.append((destinationDeb, destinationDeb + diff))
                queue.append((intersection[1]+1,seedFin))

            if intersection[0] < seedDeb <= seedFin <  intersection[1]:
                print(4)
                result.append((destinationDeb, destinationDeb + diff))
            break
        else:
            print(5)
            queue.append((seedDeb, seedFin))
            break
    if not found:
        result.append((seedDeb, seedFin))
    return result

def partTwo(parsed):
    for i in parsed:
        if i == 'seeds':
            dico = initList(parsed['seeds'])
            print(dico)
        elif i == 'seed2soil':
        # else:
            newDico = []
            print(parsed[i])
            while dico!=[]:
                range = dico.pop()
                # print(f"range{range}")
                result = convert2(range, parsed[i])
                newDico = newDico+result
            # print(newDico)
            dico = newDico
    # result = sorted(dict, key=lambda x: int(dict[x][-1]))
    sortedList = sorted(dico, key=lambda item: item[0])
    print(sortedList)
    print(f"Réponse P1 : {sortedList[0][0]}")

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    parsed = parseData(lines)
    # print(parsed)

    #Part One
    # partOne(parsed)

    #PartTwo
    partTwo(parsed) 


main()