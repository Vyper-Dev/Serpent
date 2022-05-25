import random
import os.path

Characters =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]
Characters1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]
Characters2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]
Characters3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]
Key =        []
Key2 =       []
Key3 =       []

for i in range(len(Characters1)):
	Char = random.choice(Characters1)
	Characters1.remove(Char)
	Key.append(Char)
for i in range(len(Characters2)):
	Char = random.choice(Characters2)
	Characters2.remove(Char)
	Key2.append(Char)
for i in range(len(Characters3)):
	Char = random.choice(Characters3)
	Characters3.remove(Char)
	Key3.append(Char)
	
Startup = input("Would you like to use an existing key(1) or create a new one?(2): ")
if Startup == "1":
	if os.path.exists("Key.txt"):
		f = open("Key.txt", "r")
		Key =  f.readline()
		Key2 = f.readline()
		Key3 = f.readline()
		f.close()
		
	else:
		f = open("Key.txt", "w+")
		for element in Key:
			f.write(element)
		f.write("\n")
		f = open("Key.txt", "a")
		for element in Key2:
			f.write(element)
		f.write("\n")
		f = open("Key.txt", "a")
		for element in Key3:
			f.write(element)
		f.close()
		a = open("Key.txt", "r")
		Key =  a.readline()
		Key2 = a.readline()
		Key3 = a.readline()
		a.close()
		
if Startup == "2":
	print("")
	Name = input("What would you like to name the key file?: ")
	f = open(Name + ".txt", "w+")
	for element in Key:
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
	Key =  a.readline()
	Key2 = a.readline()
	Key3 = a.readline()
	a.close()
	
while True:
	print("------------")
	print("1.Encrypt\n2.Decrypt")
	choice = input("")
	print("")
	print("Enter your message:")
	ec = list(input(""))
	
	A = 0
	B = 0
	C = 0
	
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
	
	if choice == "1":
	
		while A < len(S1):
			charpos = Characters.index(str(S1[A]))
			S1[A] = Key[charpos]
			A += 1
		while B < len(S2):
			charpos2 = Characters.index(str(S2[B]))
			S2[B] = Key2[charpos2]
			B += 1
		while C < len(S3):
			charpos3 = Characters.index(str(S3[C]))
			S3[C] = Key3[charpos3]
			C += 1
			
	if choice == "2":
	
		while A < len(S1):
			charpos = Key.index(str(S1[A]))
			S1[A] = Characters[charpos]
			A += 1
		while B < len(S2):
			charpos2 = Key2.index(str(S2[B]))
			S2[B] = Characters[charpos2]
			B += 1
		while C < len(S3):
			charpos3 = Key3.index(str(S3[C]))
			S3[C] = Characters[charpos3]
			C += 1
			
	print(*S1, *S2, *S3, sep='')
