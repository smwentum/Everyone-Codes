

def main(): 

    partOne("./TextFiles/Day Two/part1Final.txt")

def partOne(fileName):
    count = 0
    with open(fileName) as f: 
        words = f.readline()
        runicwords = words.split(":")[1].split(",")
        f.readline()
        sentence = f.readline()
        #print(sentence)
        for rune in runicwords:
            #print(rune.strip(),getNumberOfTimesSubstringAppearsInBigString(rune.strip(),sentence))
            count += getNumberOfTimesSubstringAppearsInBigString(rune.strip(),sentence)        
        print("(part one): number of runic words:",count)

def getNumberOfTimesSubstringAppearsInBigString(subString,bigString):
    return bigString.count(subString)
        

main()