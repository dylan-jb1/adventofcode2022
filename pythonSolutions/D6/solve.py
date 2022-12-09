file = open("./input.txt","r")

string = ""
stringp2 = ""
ind = 0
indp2 = 0

for line in file:
    found = False
    foundp2 = False
    for index,letter in enumerate(line):
        string += letter
        stringp2 += letter
        if len(string) >= 5:
            string = string[1:5]

            inval = False
            for index1,sletter in enumerate(string):
                for index2,sletter2 in enumerate(string):
                    if not inval and (index1 != index2) :
                        if sletter == sletter2:
                            inval = True
            
            if not found and not inval:
                ind = index
                found = True
        if len(stringp2) >= 15: #part 2
            stringp2 = stringp2[1:15]

            invalp2 = False
            for index1,sletter in enumerate(stringp2):
                for index2,sletter2 in enumerate(stringp2):
                    if not invalp2 and (index1 != index2) :
                        if sletter == sletter2:
                            invalp2 = True
            
            if not foundp2 and not invalp2:
                indp2 = index
                foundp2 = True

print(string)
print(ind+1) # part 1

print(stringp2)
print(indp2+1) # part 2