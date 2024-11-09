
def main(): 

    partOne("./TextFiles/Day One/part1Final.txt")
    partTwo("./TextFiles/Day One/part2Final.txt")
    partThree("./TextFiles/Day One/part3Final.txt")

def partOne(fileName):
    #get the string 
    count = 0
    with open(fileName) as f: 
        incommingCreatures = f.readline()
        count += getNumberOfPotionsNeeded(incommingCreatures)
    print("(part one) The number of potions needed is:",count)

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
    print("(part two) The number of potions needed is:",count)

def partThree(fileName):
    count = 0
    with open(fileName) as f: 
        incommingCreatures = f.readline()

        for i in range(0,len(incommingCreatures),3):
            #print(incommingCreatures[i:i+2])
            threeAtATime = incommingCreatures[i:i+3]
            istwoMonster = True
            #print(threeAtATime)
            monsterCount = 0
            for monster in threeAtATime:
                #print(monster) 
                if monster != 'x':
                    monsterCount+=1
                count += getNumberOfPotionsNeeded(monster)
                #print(count)
            
            if monsterCount == 3:
                count += 6
            elif monsterCount == 2:
                count += 2
            #print(count)
    print("(part three) The number of potions needed is:",count)

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