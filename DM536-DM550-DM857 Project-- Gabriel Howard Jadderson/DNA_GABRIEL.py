from enum import Enum
import time

class AminoAcid(Enum): #Enum class used to hold each aminoacid and all base-pair combinations.
    A = 'a'
    C = 'c'
    G = 'g'
    T = 't'
    A_UPPERCASE = 'A'
    C_UPPERCASE = 'C'
    T_UPPERCASE = 'T'
    G_UPPERCASE = 'G'
    AT_PAIR = 'AT'
    TA_PAIR = 'TA'
    CG_PAIR = 'CG'
    GC_PAIR = 'GC'
    # Base Pairs:  A-T, T-A,   C-G, G-C

class Container(): # only used to hold variables so they can be called statically
    result = [] #List containing our DNA-Sequence
    previousValue = None #the previousValue stored in the list or the last added element in the list.


cont = Container();  # Referencing the class to avoid any unforeseen compilation errors.

''' the following is a wrong implementation of base-pairs,ignore.
def sequenceData(DATA, charCount=-1):
    words = 0
    for letter in DATA:
        if letter == AminoAcid.A.value or letter == AminoAcid.T.value or letter == AminoAcid.G.value or letter == AminoAcid.C.value: #ignore everyting else but our aminoacids
            foundPair = False
            if cont.previousValue != None: #initially the previousValue is None, therefore, this line is false.
                if cont.previousValue == AminoAcid.A.value: #we compare the value of the previous stored letter, If the letter previously stored is A, then proceed.
                    if letter == AminoAcid.T.value: #we then check if the current letter is T
                        cont.result.pop() #we pop the last element in the list
                        cont.result.append(AminoAcid.AT_PAIR.value) #then 'AT' is appended to the end of the list
                        cont.previousValue = AminoAcid.T.value.upper() #then we update our previousValue
                        foundPair = True
                if cont.previousValue == AminoAcid.T.value:
                    if letter == AminoAcid.A.value:
                        cont.result.pop()
                        cont.result.append(AminoAcid.TA_PAIR.value)
                        cont.previousValue = AminoAcid.A.value.upper()
                        foundPair = True
                if cont.previousValue == AminoAcid.G.value:
                    if letter == AminoAcid.C.value:
                        cont.result.pop()
                        cont.result.append(AminoAcid.GC_PAIR.value)
                        cont.previousValue = AminoAcid.C.value.upper()
                        foundPair = True
                if cont.previousValue == AminoAcid.C.value:
                    if letter == AminoAcid.G.value:
                        cont.result.pop()
                        cont.result.append(AminoAcid.CG_PAIR.value)
                        cont.previousValue = AminoAcid.G.value.upper()
                        foundPair = True
            if (foundPair == False):
                cont.result.append(letter)
                cont.previousValue = letter
            words += 1
            if charCount != -1 and words >= charCount):
                print("CHARACTERS:", words)
                break
'''

def sequenceData2(DATA, charCount = -1):
    words = 0
    for letter in DATA: #Traverse over every char in the DATA string
        if letter == AminoAcid.A.value or letter == AminoAcid.T.value or letter == AminoAcid.G.value or letter == AminoAcid.C.value:  # ignore everyting else but our aminoacids
            cont.result.append(letter.upper()) #flip the letter to uppercase then append it to the list

            words += 1#DEBUG
            if charCount != -1 and words >= charCount:
                print("CHARACTERS:", words)
                break
    #print("RESULT LIST:", ''.join(cont.result))


def run(saveToFile=False, processLines = -1):
    initTime = time.clock()
    count = 0
    # using with open(args) as f:, encapsulates the file such that we can alter it, without worrying about closing the stream.
    with open("chrX.fa", "r") as f:
        f.seek(6, 0)  # set to the begning of the file. ignoring the first 6 char's in the file
        print("Processing Data...")
        for line in f:
            #sequenceData2(line.lower().strip())
            #print(line.lower().strip("n").strip("N").strip("\n").strip("").strip(" ").strip(''))
            sequenceData3(line.lower().strip("n").strip("N").strip("\n").strip("").strip(" ").strip(''))
            #print(".", end="")
            count += 1
            if processLines != -1 and count >= processLines:
                break
        print("Process Done.")
        print("RESULT: " + ''.join(cont.result))
        print("Processing Time:", round(time.clock()-initTime, 2),"seconds")

    if (saveToFile == True): #the following code is used for testing, such that the generated result can be (manually) compared to the output.
        with open("chrX_processed.fa", "w") as f:
            f.write(''.join(cont.result))

def sequenceData3(DATA):
    cont.result.append(DATA.upper())
    #print(''.join(cont.result))
run(True)