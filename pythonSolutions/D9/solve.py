import pathlib,sys,time

file = open(str(pathlib.Path(__file__).parent.resolve()) + "/input.txt")

p1=0
p2=0

headPosP1 = [0,0]
tailPosP1 = [0,0]

headPosP2 = [0,0]
tailPosP2 = [[0,0].copy()].copy()*9

visitedP1 = set()
visitedP2 = set()

maxX = [max(max([x[0] for x in tailPosP2]), headPosP2[0])]
maxY = [max(max([x[1] for x in tailPosP2]), headPosP2[1])]
minX = [min(min([x[0] for x in tailPosP2]), headPosP2[0])]
minY = [min(min([x[1] for x in tailPosP2]), headPosP2[1])]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printMapP1():
    for y in range(minY[0],maxY[0]+1):
        for x in range(minX[0],maxX[0]+1):
            printChar = f'{bcolors.WARNING}.{bcolors.ENDC}'
            if headPosP1[1] == y:
                if headPosP1[0] == x:
                    printChar = f'{bcolors.OKGREEN}H{bcolors.ENDC}'
            if tailPosP1[1] == y:
                if tailPosP1[0] == x:
                    printChar = f'{bcolors.FAIL}T{bcolors.ENDC}'
            print(printChar, end='')
        print()
    sys.stdout.write("\033[F"*((maxY[0]-minY[0])+1)) # Cursor up 3 lines

def printMapP2():
    for y in range(minY[0],maxY[0]+1):
        for x in range(minX[0],maxX[0]+1):
            printChar = f'.'
            if headPosP2[1] == y:
                if headPosP2[0] == x:
                    printChar = f'{bcolors.OKGREEN}H{bcolors.ENDC}'
            if printChar != f'{bcolors.OKGREEN}H{bcolors.ENDC}':
                for z in range(9):
                    if tailPosP2[z][1] == y:
                        if tailPosP2[z][0] == x:
                            printChar = f'{bcolors.WARNING}{str(z+1)}{bcolors.ENDC}'
                            break
            print(printChar, end='')
        print()
    sys.stdout.write("\033[F"*((maxY[0]-minY[0])+1))

def adjustTail():
    if ((headPosP1[0] - tailPosP1[0]) > 1): # head is to the right of tail
        tailPosP1[0]+=1
        if ((headPosP1[1] - tailPosP1[1]) > 0):
            tailPosP1[1]+=1
        elif ((headPosP1[1] - tailPosP1[1]) < 0):
            tailPosP1[1]-=1
    elif ((headPosP1[0] - tailPosP1[0]) < -1): # head is to the left of tail
        tailPosP1[0]-=1
        if ((headPosP1[1] - tailPosP1[1]) > 0):
            tailPosP1[1]+=1
        elif ((headPosP1[1] - tailPosP1[1]) < 0):
            tailPosP1[1]-=1
    if ((headPosP1[1] - tailPosP1[1]) > 1): # head is above tail
        tailPosP1[1]+=1
        if ((headPosP1[0] - tailPosP1[0]) > 0):
            tailPosP1[0]+=1
        elif ((headPosP1[0] - tailPosP1[0]) < 0):
            tailPosP1[0]-=1
    elif ((headPosP1[1] - tailPosP1[1]) < -1): # head is below tail
        tailPosP1[1]-=1
        if ((headPosP1[0] - tailPosP1[0]) > 0):
            tailPosP1[0]+=1
        elif ((headPosP1[0] - tailPosP1[0]) < 0):
            tailPosP1[0]-=1

    visitedP1.add((tailPosP1[0],tailPosP1[1]))
    

def adjustTailP2(n):
    ahead = headPosP2
    if (n == 0):
        ahead = headPosP2
    else:
        ahead = tailPosP2[n-1]

    curTail = tailPosP2[n].copy()

    if ((ahead[0] - curTail[0]) > 1): # head is to the right of tail
        curTail[0]+=1
        if ((ahead[1] - curTail[1]) > 0):
            curTail[1]+=1
        elif ((ahead[1] - curTail[1]) < 0):
            curTail[1]-=1
    elif ((ahead[0] - curTail[0]) < -1): # head is to the left of tail
        curTail[0]-=1
        if ((ahead[1] - curTail[1]) > 0):
            curTail[1]+=1
        elif ((ahead[1] - curTail[1]) < 0):
            curTail[1]-=1
    if ((ahead[1] - curTail[1]) > 1): # head is above tail
        curTail[1]+=1
        if ((ahead[0] - curTail[0]) > 0):
            curTail[0]+=1
        elif ((ahead[0] - curTail[0]) < 0):
            curTail[0]-=1
    elif ((ahead[1] - curTail[1]) < -1): # head is below tail
        curTail[1]-=1
        if ((ahead[0] - curTail[0]) > 0):
            curTail[0]+=1
        elif ((ahead[0] - curTail[0]) < 0):
            curTail[0]-=1

    if (n==8):
        visitedP2.add((curTail[0],curTail[1]))
    
    tailPosP2[n] = curTail

    maxX[0] = max(max([x[0] for x in tailPosP2]), headPosP2[0],maxX[0])
    maxY[0] = max(max([x[1] for x in tailPosP2]), headPosP2[1],maxY[0])
    minX[0] = min(min([x[0] for x in tailPosP2]), headPosP2[0],minX[0])
    minY[0] = min(min([x[1] for x in tailPosP2]), headPosP2[1],minY[0])
    printMapP2()
    time.sleep(0.1/9)

for line in file:
    lineSplit=line.split()
    if (lineSplit[0] == "R"):
        for x in range(int(lineSplit[1])):
            headPosP1[0]+=1
            headPosP2[0]+=1
            adjustTail()
            for z in range(9):
                adjustTailP2(z)
    elif (lineSplit[0] == "U"):
        for x in range(int(lineSplit[1])):
            headPosP1[1]+=1
            headPosP2[1]+=1
            adjustTail()
            for z in range(9):
                adjustTailP2(z)
    elif (lineSplit[0] == "L"):
        for x in range(int(lineSplit[1])):
            headPosP1[0]-=1
            headPosP2[0]-=1
            adjustTail()
            for z in range(9):
                adjustTailP2(z)
    elif (lineSplit[0] == "D"):
        for x in range(int(lineSplit[1])):
            headPosP1[1]-=1
            headPosP2[1]-=1
            adjustTail()
            for z in range(9):
                adjustTailP2(z)
    

p1 = len(visitedP1)
p2 = len(visitedP2)

print(p1) #part 1
print(p2) #part 2