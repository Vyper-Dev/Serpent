import random
import os.path

Characters  = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", "[" , "]", "(", ")", "\n"]

def Sort(ec):
    global S1
    global S2
    global S3
    String_Length = len(ec)
    Section_Length = String_Length / 3
    Start = 0
    Stop = int(Section_Length)
    Section_Length = int(Section_Length)
    Start = int(Start)
    Stop = int(Stop)
    S1 = ec[Start : Stop]
    Start = Start + Section_Length
    Stop = Stop + Stop
    S2 = ec[Start : Stop]
    Start = Start + Section_Length
    Stop = Stop + Stop
    S3 = ec[Start : len(ec)]
    Start = Start + Section_Length
    Stop = Stop + Stop
    return S1, S2, S3

def Encrypt(S1,S2,S3):
    for i in range(len(S1)):
        try:
            charpos = Characters.index(str(S1[i]))
            S1[i] = Key1[charpos]
        except:
            pass
    for i in range(len(S2)):
        try:
            charpos2 = Characters.index(str(S2[i]))
            S2[i] = Key2[charpos2]
        except:
            pass
    for i in range(len(S3)):
        try:
            charpos3 = Characters.index(str(S3[i]))
            S3[i] = Key3[charpos3]
        except:
            pass
    return S1, S2, S3

def Decrypt(S1,S2,S3):
    for i in range(len(S1)):
        try:
            charpos = Key1.index(str(S1[i]))
            S1[i] = Characters[charpos]
        except:
            pass
    for i in range(len(S2)):
        try:
            charpos2 = Key2.index(str(S2[i]))
            S2[i] = Characters[charpos2]
        except:
            pass
    for i in range(len(S3)):
        try:
            charpos3 = Key3.index(str(S3[i]))
            S3[i] = Characters[charpos3]
        except:
            pass
    return S1, S2, S3

def GenKey(Name):
    global Key1
    global Key2
    global Key3
    Key1 = []
    Key2 = []
    Key3 = []
    Characters1 = Characters[:-1]
    Characters2 = Characters[:-1]
    Characters3 = Characters[:-1]
    for i in range(len(Characters1)):
        Char = random.choice(Characters1)
        Characters1.remove(Char)
        Key1.append(Char)
    for i in range(len(Characters2)):
        Char = random.choice(Characters2)
        Characters2.remove(Char)
        Key2.append(Char)
    for i in range(len(Characters3)):
        Char = random.choice(Characters3)
        Characters3.remove(Char)
        Key3.append(Char)
    f = open(Name, "w")
    for element in Key1:
        f.write(element)
    f.write("\n")
    f = open(Name, "a")
    for element in Key2:
        f.write(element)
    f.write("\n")
    f = open(Name, "a")
    for element in Key3:
        f.write(element)
    f.close()
    return Key1, Key2, Key3
    
def OpenKey(Name):
    global Key1
    global Key2
    global Key3
    if os.path.exists(Name):
            f = open(Name, "r")
            Key1 =  f.readline()
            Key2 = f.readline()
            Key3 = f.readline()
            f.close()
            print(Key1, Key2, Key3)
            return Key1, Key2, Key3
    else:
        print("No key file found with that name. Please re-enter your key file name.")
        return False

def Save(Name):
    f = open(Name, "w")
    for element in S1:
        f.write(element)
    f = open(Name, "a")
    for element in S2:
        f.write(element)
    f = open(Name, "a")
    for element in S3:
        f.write(element)
    f.close()

def ReadFile(Name):
    global ec
    f = open(Name, "r")
    ec = list(''.join(f.readlines()))
    f.close()
    print(ec)
    return ec