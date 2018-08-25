from enum import Enum

class AminoAcid(Enum):
    A = 'a'
    C = 'c'
    G = 'g'
    T = 't'
    AT_PAIR = 'AT'
    TA_PAIR = 'TA'
    CG_PAIR = 'CG'
    GC_PAIR = 'GC'
    # Base Pairs: A-T, C-G


for AminoAcid in AminoAcid:
    print(
        AminoAcid.name + " = " + AminoAcid.value)

# used as a nullcheck just to make sure the file is opened and/or not empty.

class Container(): #only used to hold variables so i can call them statically
    result = []
    list = []
    iterator = 0
    data = None
    lastLetter = None
    firstRun = True

cont = Container(); #Referencing the class to avoid any unforeseen compilation errors.

print(len(cont.result))

def processLine(line, lineCount):
    global cont
    cont.data = line.lower().strip()  # turn all the chars in the search-string to lowercase since we can ignore uppercase. Then we strip the string of all whitespace characters, python has a neat built-in string func called stripline.lower().strip():() which does this for us.
    print(cont.data)
    for i in cont.data:
        if i == 'N': continue
        if i == 'n': continue
        if len(cont.list) >= 1:
            if (cont.lastLetter != None):
                if (cont.lastLetter == AminoAcid.A.value and i == AminoAcid.T.value):
                    cont.result.append(AminoAcid.AT_PAIR.value)
            if (cont.list[cont.iterator-1] == AminoAcid.A.value) and (i == AminoAcid.T.value):
                print("found AT base pairs")
                cont.result.append(AminoAcid.AT_PAIR.value)
            elif (cont.list[cont.iterator-1] == AminoAcid.T.value) and (i == AminoAcid.A.value):
                print("found TA base pairs")
                cont.result.append(AminoAcid.TA_PAIR.value)
            elif (cont.list[cont.iterator-1] == AminoAcid.C.value) and (i == AminoAcid.G.value):
                print("found CG base pairs")
                cont.result.append(AminoAcid.CG_PAIR.value)
            elif (cont.list[cont.iterator-1] == AminoAcid.G.value) and (i == AminoAcid.C.value):
                print("found GC base pairs")
                cont.result.append(AminoAcid.GC_PAIR.value)
            if i == AminoAcid.A.value:
                cont.list.append(i)
                cont.result.append(i)
            elif i == AminoAcid.C.value:
                cont.list.append(i)
                cont.result.append(i)
            elif i == AminoAcid.T.value:
                cont.list.append(i)
                cont.result.append(i)
            elif i == AminoAcid.G.value:
                cont.list.append(i)
                cont.result.append(i)
        else:
            if i == AminoAcid.A.value: cont.list.append(i)
            elif i == AminoAcid.C.value: cont.list.append(i)
            elif i == AminoAcid.T.value: cont.list.append(i)
            elif i == AminoAcid.G.value: cont.list.append(i)
        cont.iterator += 1
        cont.lastLetter = cont.data[len(cont.data)-1]
        print(cont.lastLetter)
    #print(cont.iterator)
    #print(cont.data[0])
    #print(cont.data[1])
    #print(cont.data[2])
    #print(cont.data[3])
    #print(cont.data[4])
        if (lineCount >= 206):
            print("RESULT: " + ''.join(cont.result))
            exit(100)

        # while iterator <= charCount:
        #   if '>chrX' in data: continue
        #  if 'N' in data: continue
        # if 'n' in data: continue
        # list.append(data)
        # iterator += 1
        # if (len(list) >= 1):
        # print(list[iterator-1])
        # if (list[iterator-1] == AminoAcid.A):
        # if (i == AminoAcid.T):
        # print("found AT with iteration", iterator)
        # if AminoAcid.A.value in list: print(i)

def processData(RAW_DATA):
    wordsProcessed = 0
    for i in RAW_DATA:
        if i == 'N': continue
        if i == 'n': continue

        if (cont.lastLetter == None):#first time assignment
            cont.lastLetter = i
            continue
        if (cont.lastLetter == AminoAcid.A.value and i == AminoAcid.T.value):
                cont.result.append(AminoAcid.AT_PAIR.value)
        elif (cont.lastLetter == AminoAcid.T.value and i == AminoAcid.A.value):
                cont.result.append(AminoAcid.TA_PAIR.value)
        elif (cont.lastLetter == AminoAcid.G.value and i == AminoAcid.C.value):
                cont.result.append(AminoAcid.GC_PAIR.value)
        elif (cont.lastLetter == AminoAcid.C.value and i == AminoAcid.G.value):
            cont.result.append(AminoAcid.CG_PAIR.value)
        elif (i == AminoAcid.A.value): cont.result.append(i)
        elif (i == AminoAcid.C.value): cont.result.append(i)
        elif (i == AminoAcid.G.value): cont.result.append(i)
        elif (i == AminoAcid.T.value): cont.result.append(i)


        cont.result.append(i)


        cont.lastLetter = i
        cont.iterator += 1

        wordsProcessed += 1
        print("i", i)
        if (wordsProcessed >= 290):
            print("RESULT: " + ''.join(cont.result))
            exit(100)


def processData2(DATA):
    for letter in DATA:
        if (letter == 'N'): continue
        if (letter == 'n'): continue
        if (letter == AminoAcid.A.value or letter == AminoAcid.C.value or letter == AminoAcid.T.value or letter == AminoAcid.G.value):
            if (cont.firstRun == True):
                cont.result.append(letter)
                cont.iterator += 1
                cont.firstRun = False
                continue
            else:
                if cont.result[cont.iterator] == AminoAcid.A.value and letter == AminoAcid.T.value:
                    cont.result.append(AminoAcid.AT_PAIR.value)
                    cont.iterator += 1
                elif cont.result[cont.iterator] == AminoAcid.T.value and letter == AminoAcid.A.value:
                    cont.result.append(AminoAcid.TA_PAIR.value)
                    cont.iterator += 1
                elif cont.result[cont.iterator] == AminoAcid.C.value and letter == AminoAcid.G.value:
                    cont.result.append(AminoAcid.CG_PAIR.value)
                    cont.iterator += 1
                elif cont.result[cont.iterator] == AminoAcid.G.value and letter == AminoAcid.C.value:
                    cont.result.append(AminoAcid.GC_PAIR.value)
                    cont.iterator += 1
                else:
                    cont.result.append(letter)
                    cont.iterator += 1
    print(cont.result)





# using with open(args) as f:, encapsulates the file such that we can alter it, without worrying about closing the stream.
with open("chrX.fa", "r") as f:
    f.seek(6, 0)  # set to the begning of the file. ignoring the first 6 char's in the file
    lines = 0
    chars = 0
    cont.data = f.read().lower().strip()
    #processData(cont.data)
    processData2(cont.data)
    it = 0
    for line in f:
        lines += 1
        chars += len(line)
        #processLine(line, lines)
    f.seek(6, 0)
    #while it <= chars:
        #print(f.read(1))
    print("lines:", lines, "chars:", chars)

    '''
    while x <= chars:
        for i in data:
            data = f.read(x)
            print(i)
            if 'N' in i: continue
            if '>chrX' in i: continue
            if AminoAcid.AT_PAIR.value in i: print(i)


        x += 50 #assuming each line is 50 char's long
        data = f.read(x)
        '''


def calculateNextIndices(previousIndex):
    return previousIndex + 50

'''
N_TOTAL_COUNT = cont.data.count("N")
A_TOTAL_COUNT = cont.data.count("A") + cont.data.count("a")
C_TOTAL_COUNT = cont.data.count("C") + cont.data.count("c")
G_TOTAL_COUNT = cont.data.count("G") + cont.data.count("g")
T_TOTAL_COUNT = cont.data.count("T") + cont.data.count("t")

print("Found " + str(
    A_TOTAL_COUNT) + " Occurrences of adenine")
print("Found " + str(
    C_TOTAL_COUNT) + " Occurrences of cytosine")
print("Found " + str(
    G_TOTAL_COUNT) + " Occurrences of guanine")
print("Found " + str(
    T_TOTAL_COUNT) + " Occurrences of thymine")
'''
