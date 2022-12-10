import pathlib

file = open(str(pathlib.Path(__file__).parent.resolve()) + "/input.txt")

p1=0
p2=0

cycle = 0
cycleUp = 0

xReg = 1

c20 = []

pixels = [0].copy()*240

for line in file:
    sl = line.split()

    addVal = 0

    if (sl[0] == "addx"):
        cycleUp=cycle+2
        addVal = int(sl[1])
    elif (sl[0] == "noop"):
        cycleUp=cycle+1

    while (cycle < cycleUp):
        cycle+=1
        #pixeldraw
        pixelsSpr = [xReg-1,xReg,xReg+1]
        if (pixelsSpr[0]==((cycle-1)%40) or pixelsSpr[1]==((cycle-1)%40) or pixelsSpr[2]==((cycle-1)%40)):
            pixels[(cycle-1)%240] = 1
        if (cycle == 20 or (cycle>20 and ((cycle-20)%40) == 0)):
            c20.append(cycle*xReg)

    xReg+= addVal

for index,pixel in enumerate(pixels):
    if (index%40)==0:
        print()
    print("#",end='') if pixel==1 else print(".",end='')
print()

print(p1) #part 1
print(p2) #part 2