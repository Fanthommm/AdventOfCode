times =  [57,72,69,92]
distances = [291,1172,1176,2026]

def partOne():
    total = 1
    for i in range(len(times)):
        winningTrys = 0
        time = times[i]
        record = distances[i]
        for hold in range(time):
            distance = hold*(time-hold)
            if distance > record:
                winningTrys+=1
        total *= winningTrys
    
    print(f"PART ONE : réponse : {total}")
        
def partTwo():
    winningTrys = 0
    time = 57726992
    record = 291117211762026
    for hold in range(time):
        distance = hold*(time-hold)
        if distance > record:
            winningTrys+=1
    total = winningTrys
    
    print(f"PART ONE : réponse : {total}")

def main():
    partOne()

    partTwo()

main()