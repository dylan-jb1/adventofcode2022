import pathlib

p1=0
p2=0

monkeyDict = dict()
monkeyCount = dict()

class Monkey:
    test: int
    listVals: list
    op: list

rounds = 1000
for x in range(rounds):
    lines = [""].copy()*6
    iter = 0

    multTotal = 1

    file = open(str(pathlib.Path(__file__).parent.resolve()) + "/input.txt")
    for line in file:
        if (iter > 0 and iter % 6 == 0):
            monkeyId = int(lines[0].split(" ")[1].split(":")[0])
            items = lines[1].split(": ")[1].split(", ")
            oper = lines[2].split("new = ")[1]
            test = int(lines[3].split("divisible by ")[1])
            trueId = int(lines[4].split("to monkey ")[1])
            falseId = int(lines[5].split("to monkey ")[1])

            if x==0: 
                if monkeyId in monkeyDict:
                    items = monkeyDict[monkeyId].listVals + items
                else:
                    newMonkey = Monkey()
                    newMonkey.test=test
                    multTotal*=test
                    newMonkey.op=oper
                    newMonkey.listVals = items.copy()
                    monkeyDict[monkeyId] = newMonkey
            else: items= monkeyDict[monkeyId].listVals

            lines = [""].copy()*6

            for item in items:
                if monkeyId in monkeyCount:
                    monkeyCount[monkeyId]+=1
                else:
                    monkeyCount[monkeyId]=1

                operEval = oper.replace("old",str(item))
                newWorry = eval(operEval)
                if newWorry%test==0:
                    if trueId in monkeyDict:
                        monkeyDict[trueId].listVals.append(newWorry if x==0 else newWorry%multTotal)
                    else:
                        newMonkey = Monkey()
                        newMonkey.listVals = [newWorry]
                        monkeyDict[trueId] = newMonkey
                else:
                    if falseId in monkeyDict:
                        monkeyDict[falseId].listVals.append(newWorry if x==0 else newWorry%multTotal)
                    else:
                        newMonkey = Monkey()
                        newMonkey.listVals = [newWorry]
                        monkeyDict[falseId] = newMonkey
            monkeyDict[monkeyId].listVals.clear()
            iter=-1
        else:
            lines[iter%6]=line.strip()
        iter+=1
    file.close()

print(monkeyCount)
monkeyVals = list(monkeyCount.values())
monkeyVals.sort(reverse=True)
p1= monkeyVals[0]*monkeyVals[1]

print(p1) #part 1
print(p2) #part 2