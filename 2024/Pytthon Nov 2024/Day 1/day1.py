
def main(): 

    partOne("./part1Final.txt")

def partOne(fileName):
    #get the string 
    count = 0
    with open(fileName) as f: 
        incommingCreatures = f.readline()
        for creature in incommingCreatures:
            match creature:
                case 'B':
                    count += 1
                case 'C':
                    count += 3
    print("The number of potions needed is:",count)
            
main()