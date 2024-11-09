
def main(): 

    partOne("./part1Final.txt")
    partTwo("./part2Final.txt")

def partOne(fileName):
    #get the string 
    count = 0
    with open(fileName) as f: 
        incommingCreatures = f.readline()
        count += getNumberOfPotionsNeeded(incommingCreatures)
    print("The number of potions needed is:",count)

def partTwo(fileName):
    count = 0
    with open(fileName) as f: 
        incommingCreatures = f.readline()

        for i in range(0,len(incommingCreatures),2):
            #print(incommingCreatures[i:i+2])
            twoAtATime = incommingCreatures[i:i+2]
            istwoMonster = True
            for monster in twoAtATime: 
                if monster == 'x':
                    istwoMonster = False
                count += getNumberOfPotionsNeeded(monster)
            if istwoMonster:
                count += 2
    print("The number of potions needed is:",count)

def getNumberOfPotionsNeeded(incommingCreatrues):
    count= 0
    for creature in incommingCreatrues:
            match creature:
                case 'B':
                    count += 1
                case 'C':
                    count += 3
                case 'D':
                    count += 5
    return count

main()