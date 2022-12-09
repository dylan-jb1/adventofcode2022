file = open("./input.txt", "r")


class TreeNode:
    location: int
    size: int
    parent: object
    children: list
    def __init__(self,location,size,parent,children):
        self.location = location
        self.size=size
        self.parent=parent
        self.children=children
    
    def getPath(self):
        curEl = self
        pathString = ""
        while (curEl.parent != None):
            pathString = ("/" + str(curEl.location) ) + pathString
            curEl = curEl.parent
        return pathString

dirHead = TreeNode("/", 0, None, [])
curDir = dirHead
dirMap = dict({"/":dirHead}) # key: (size, parent, children)

print(dirHead.getPath())

for line in file:
    res = line.split()
    if res[0] == "$": #command
        if res[1] == "cd":
            if res[2] == "..":
                curDir = curDir.parent
            elif res[2] == "/":
                curDir = dirHead
            else:
                curDir = dirMap[curDir.getPath() + "/" + res[2]]
    elif res[0] == "dir": #directory
        if (curDir.getPath() + "/" + res[1]) not in dirMap:
            dirMap[(curDir.getPath() + "/" + res[1])] = TreeNode(res[1],0,curDir,[])
        curDir.children.append(dirMap[curDir.getPath() + "/" + res[1]])
    elif res[0].isnumeric(): # file
        curDir.size+=int(res[0])
        curParent = curDir.parent
        while curParent != None:
            curParent.size+=int(res[0])
            curParent = curParent.parent

p1 = 0
for key,value in dirMap.items():
    if value.size<=100000:
        p1+=value.size

p2 = 0
closest = [None,30000000]
print("space: ", (30000000-(70000000-dirHead.size)))
for key,value in dirMap.items():
    distance = value.size - (30000000-(70000000-dirHead.size))
    if ( distance > 0 and distance < closest[1]):
        closest = [value, value.size]
p2 = closest[1]

print(p1) # part 1
print(p2) # part 2


print(closest[0].location, closest[1])