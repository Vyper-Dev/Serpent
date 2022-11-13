import random
import os.path

Characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]
Characters1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]
Characters2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]
Characters3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]

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
    f = open(Name + ".txt", "w+")
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
    a = open(Name + ".txt", "r")
    Key1 =  a.readline()
    Key2 = a.readline()
    Key3 = a.readline()
    a.close()

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

while True:
	Startup = input("Would you like to use an existing key(1) or create a new one?(2): ")
	if Startup == "1":
		Name = input("\nWhat is the name of your key file? (No extension): ")
		if os.path.exists(Name + ".txt"):
			f = open(Name + ".txt", "r")
			Key1 =  f.readline()
			Key2 = f.readline()
			Key3 = f.readline()
			f.close()
			break
		if Name == "":
			print("Key file names cannot be blank. Please re-enter a key file name.")
	if Startup == "2":
		Name = input("\nWhat would you like to name the key file? (No extension): ")
		GenKey()
		if Name == "":
			print("Key file names cannot be blank. Please re-enter a key file name.")
		break
	
while True:
	A = 0
	B = 0
	C = 0
	choice = input("\n------------\n1.Encrypt\n2.Decrypt\nChoice: ")
	ec = list(input("\nEnter your message: "))
	Sort()
	if choice == "1":
		Encrypt()
	if choice == "2":
		Decrypt()
	print(f"Output: ", *S1, *S2, *S3, sep='')