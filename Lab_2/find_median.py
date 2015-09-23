import sys
#Class/Function definition
if __name__=='__main__': #make sure when you import a file it does not run
    myList = []
    for fileName in sys.argv[1:]:
        inputFile = open(fileName, 'r') #open the file
        for line in inputFile:
            myList.append(int(line.strip()))
    myList.sort()
    print myList[len(myList)/2]
    
