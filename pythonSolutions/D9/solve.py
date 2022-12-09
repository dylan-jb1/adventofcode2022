import pathlib

file = open(str(pathlib.Path(__file__).parent.resolve()) + "/input.txt")

p1=0
p2=0

headPosP1 = [0,0]
tailPosP1 = [0,0]

headPosP2 = [0,0]
tailPosP2 = [[0,0].copy()].copy()*9

visitedP1 = set()
visitedP2 = set()

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