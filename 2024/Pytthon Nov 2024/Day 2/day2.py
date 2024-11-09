import re

def main(): 

    partOne("./TextFiles/Day Two/part1Final.txt")
    partTwo("./TextFiles/Day Two/part2test.txt")

    partTwo("./TextFiles/Day Two/part2Final.txt")

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

def partTwo(fileName):
    count = 0
    with open(fileName) as f: 
        words = f.readline()
        runicwords = words.split(":")[1].split(",")
        f.readline()
        runicwords.sort()
        sent = ''
        for  sentence in f.readlines():
            sent += sentence.strip()
        sent.strip()
       # for  sentence in f.readlines():
        #sentence = sentence.strip()
        #print(sentence)
        #print(sent)
        bitArray =  [False]*len(sent)
        for rune in runicwords:
            rune = rune.strip()
            #if not str.isspace(rune):
            bitArray=updateMarkedLetterInSentence(rune[::-1],sent,bitArray)
            bitArray=updateMarkedLetterInSentence(rune,sent,bitArray)
                
        count += sum(bitArray) 
        #dup = set()
        # for rune in runicwords:
        #         rune = rune.strip()
        #         #print(rune)
        #         if rune[::-1] in dup:
        #             print("there is a dup ", rune[::-1])

        print("(part two): number of runic words:",count)

def getNumberOfTimesSubstringAppearsInBigString(subString,bigString):
    count  = bigString.count(subString) 
    #if count > 0:
    #    print(f"{subString}: {count}",)
    return count
def updateMarkedLetterInSentence(substring,bigString,bytyeArray):
    for i in [m.start() for m in re.finditer(substring,bigString)]:
        for j in range(i,i+len(substring)):
            bytyeArray[j] = True
    return bytyeArray





main()