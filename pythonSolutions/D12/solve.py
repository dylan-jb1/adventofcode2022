import pathlib,queue

file = open(str(pathlib.Path(__file__).parent.resolve()) + "/input.txt")

p1=0
p2=0


grid = []

startM = [0,0]
endM = [0,0]

for indexy,line in enumerate(file):
    gridString = ""
    for indexx,char in enumerate(line.strip()):
        if char == 'S':
            gridString+='a'
            startM=[indexx,indexy]
        elif char=='E':
            gridString+='z'
            endM=[indexx,indexy]
        else:
            gridString+=char
    grid.append(gridString)

def checkMoves(loc):
    moves = []
    if (loc[1]-1)>=0 and (ord(grid[loc[1]][loc[0]].lower())-ord(grid[loc[1]-1][loc[0]].lower())>=-1): #up
        moves.append([loc[0],loc[1]-1])
    if (loc[1]+1)<len(grid) and (ord(grid[loc[1]][loc[0]].lower())-ord(grid[loc[1]+1][loc[0]].lower())>=-1): #down
        moves.append([loc[0],loc[1]+1])
    if (loc[0]-1)>=0 and (ord(grid[loc[1]][loc[0]].lower())-ord(grid[loc[1]][loc[0]-1].lower())>=-1): #left
        moves.append([loc[0]-1,loc[1]])
    if (loc[0]+1)<len(grid[0]) and (ord(grid[loc[1]][loc[0]].lower())-ord(grid[loc[1]][loc[0]+1].lower())>=-1): #right
        moves.append([loc[0]+1,loc[1]])

    return moves.copy()

def bfs(start,end):
    bfsQueue = [[start,[]]]
    bfsVisited = set()
    while (len(bfsQueue) > 0):
        cur = bfsQueue.pop(0)
        if cur[0]==end:
            return cur[1]
        for move in checkMoves(cur[0]):
            if (move.copy()[0],move.copy()[1]) not in bfsVisited:
                bfsQueue.append([move.copy(),cur[1]+[move.copy()]])
                bfsVisited.add((move.copy()[0],move.copy()[1]))

path = bfs(startM,endM)
p1=len(path)

p2 = None

for indexy,line in enumerate(grid):
    for indexx,char in enumerate(line.strip()):
        if char=='a':
            path = bfs([indexx,indexy],endM)
            if p2==None or (path!=None and len(path)<p2):
                p2=len(path)

print(p1) #part 1
print(p2) #part 2