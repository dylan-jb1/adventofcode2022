import pathlib

file = open(str(pathlib.Path(__file__).parent.resolve()) + "/input.txt")

p1=0
p2=0

treeGrid = []

for line in file:
    rowString = ""
    for index,letter in enumerate(line):
        if (letter != "\n"):
            rowString+=letter
    treeGrid+=rowString.split()

visible = [[0 for x in range(len(treeGrid[0]))] for x in range(len(treeGrid))]

columnTopMaxHeight = [-1 for x in range(len(treeGrid))]
columnBottomMaxHeight = [-1 for x in range(len(treeGrid))]
rowLeftMaxHeight = [-1 for x in range(len(treeGrid[0]))]
rowRightMaxHeight = [-1 for x in range(len(treeGrid[0]))]

leftScene = [[0 for x in range(len(treeGrid[0]))] for x in range(len(treeGrid))]
rightScene = [[0 for x in range(len(treeGrid[0]))] for x in range(len(treeGrid))]
topScene = [[0 for x in range(len(treeGrid[0]))] for x in range(len(treeGrid))]
bottomScene = [[0 for x in range(len(treeGrid[0]))] for x in range(len(treeGrid))]

for rowIndex,row in enumerate(treeGrid): # top to bottom
    for columnIndex,column in enumerate([int(x) for x in row]): #forwards
        if column > rowLeftMaxHeight[rowIndex]:
            rowLeftMaxHeight[rowIndex] = column
            visible[rowIndex][columnIndex]=1
        if column > columnTopMaxHeight[columnIndex]:
            columnTopMaxHeight[columnIndex] = column
            visible[rowIndex][columnIndex]=1

        vis = 0
        for index,x in enumerate(row):
            if (columnIndex != index):
                if x < column:
                    vis+=1
                else: vis=1

        for indexLeft,columnScene in enumerate([int(x) for x in reversed(row[:columnIndex])]): # left
            if columnScene < column:
                leftScene[rowIndex][columnIndex]+=1
            else:
                leftScene[rowIndex][columnIndex]+=1
                break
        for indexRight,columnScene in enumerate([int(x) for x in row[columnIndex+1:]]): # right
            if columnScene < column:
                rightScene[rowIndex][columnIndex]+=1
            else:
                rightScene[rowIndex][columnIndex]+=1
                break
        for indexTop,rowScene in enumerate(reversed(treeGrid[:rowIndex])): # top
            if int(rowScene[columnIndex]) < column:
                topScene[rowIndex][columnIndex]+=1
            else:
                topScene[rowIndex][columnIndex]+=1
                break
        for indexBottom,rowScene in enumerate(treeGrid[rowIndex+1:]): # bottom
            if int(rowScene[columnIndex]) < column:
                bottomScene[rowIndex][columnIndex]+=1
            else:
                bottomScene[rowIndex][columnIndex]+=1
                break
    for columnIndex,column in enumerate(reversed([int(x) for x in row])): # backwards
        if column > rowRightMaxHeight[rowIndex]:
            rowRightMaxHeight[rowIndex] = column
            visible[rowIndex][(len(treeGrid[0])-1)-columnIndex]=1
for rowIndex,row in enumerate(reversed(treeGrid)): #bottom to top
    for columnIndex,column in enumerate([int(x) for x in row]): #forwards
        if column > columnBottomMaxHeight[columnIndex]:
            columnBottomMaxHeight[columnIndex] = column
            visible[(len(treeGrid[0])-1)-rowIndex][columnIndex]=1
        
p1 = sum([sum(x) for x in visible])

sceneScore = [[a*b*c*d for a,b,c,d in zip(topScene[x],bottomScene[x],leftScene[x],rightScene[x])] for x in range(len(topScene))]

p2 = max([max(x) for x in sceneScore])

print(p1) #part 1
print(p2) #part2