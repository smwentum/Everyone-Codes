
def main(): 

    partOne("./part1Final.txt")

def partOne(fileName):
    #get the string 
    count = 0
    with open(fileName) as f: 
        incommingCreatures = f.readline()
        count += getNumberOfPotionsNeeded(incommingCreatures)
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