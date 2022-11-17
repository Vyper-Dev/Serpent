import random
import os.path

Characters  = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", "\n"]
Characters1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", "\n"]
Characters2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", "\n"]
Characters3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", "\n"]
Key1 = []
Key2 = []
Key3 = []

def Sort():
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

def Encrypt():
    A = 0
    B = 0
    C = 0
    while A < len(S1):
        try:
            charpos = Characters.index(str(S1[A]))
            S1[A] = Key1[charpos]
        except ValueError:
            S1[A] = S1[A]
        A += 1
    while B < len(S2):
        try:
            charpos2 = Characters.index(str(S2[B]))
            S2[B] = Key2[charpos2]
        except ValueError:
            S2[B] = S2[B]
        B += 1
    while C < len(S3):
        try:
            charpos3 = Characters.index(str(S3[C]))
            S3[C] = Key3[charpos3]
        except ValueError:
            S3[C] = S3[C]
        C += 1

def Decrypt():
    A = 0
    B = 0
    C = 0
    while A < len(S1):
        try:
            charpos = Key1.index(str(S1[A]))
            S1[A] = Characters[charpos]
        except ValueError:
            S1[A] = S1[A]
        A += 1
    while B < len(S2):
        try:
            charpos2 = Key2.index(str(S2[B]))
            S2[B] = Characters[charpos2]
        except ValueError:
            S2[B] = S2[B]
        B += 1
    while C < len(S3):
        try:
            charpos3 = Key3.index(str(S3[C]))
            S3[C] = Characters[charpos3]
        except ValueError:
            S3[C] = S3[C]
        C += 1

def GenKey():
    global Key1
    global Key2
    global Key3
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
    f = open(Name + ".txt", "w")
    for element in Key1:
        f.write(element)
    f.write("\n")
    f = open(Name + ".txt", "a")
    for element in Key2:
        f.write(element)
    f.write("\n")
    f = open(Name + ".txt", "a")
    for element in Key3:
        f.write(element)
    f.close()

def OpenKey():
    global Key1
    global Key2
    global Key3
    if os.path.exists(Name + ".txt"):
            f = open(Name + ".txt", "r")
            Key1 =  f.readline()
            Key2 = f.readline()
            Key3 = f.readline()
            f.close()
            return True
    else:
        print("No key file found with that name. Please re-enter your key file name.")
        return False

def Save():
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

while True:
    Startup = input("Select an option:\n (1) Existing key\n (2) Generate key\n\n Option: ")
    Name = input("\nEnter keyfile name (without extension): ")
    if Name == "" or Name == " ":
            print("Keyfile names cannot be blank.")
    if Startup == "1":
        if OpenKey() == True:
            break
    if Startup == "2":
        GenKey()
        OpenKey()
        break

while True:
    choice = input("-------------------------------\nSelect a Method:\n (1) Encrypt\n (2) Decrypt\n (3) Back\n Method: ")
    if choice == "3":
        break
    ec = list(input("-------------------------------\nEnter the message: "))
    Sort()
    if choice == "1":
        Encrypt()
    if choice == "2":
        Decrypt()
    print(*S1, *S2, *S3, sep='')