Characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?"]
Key =        ['e', 'v', '5', '?', 'F', 'H', 'w', 'N', 'I', 'T', 'K', 'C', 'L', 'o', 'k', 'E', '3', 't', 'l', '0', 'n', 'x', 'z', 'p', 'q', 'J', 'c', 'S', 'j', 'b', 'm', '1', '6', 'i', 's', '7', 'y', 'Y', '!', 'M', '8', 'd', 'f', 'W', 'a', 'B', '.', 'U', 'G', '9', 'Z', 'r', 'Q', '2', ',', 'X', 'P', 'u', 'g', 'R', ' ', 'h', 'V', 'O', 'D', '4', 'A']
Key2 =       ['Q', 'j', 'u', 'D', '9', 'M', 'W', 'Z', 'q', 'b', '7', 'o', '3', 'z', 'r', 'H', '5', 'O', 'm', 'f', 'V', 'p', 'w', 'y', ',', 'k', 'U', 'e', 'E', 'K', 'G', '4', '!', '.', '2', 't', 'n', 'T', ' ', 'Y', 'h', '8', 'a', 'd', '?', 'x', 'g', 'J', 'C', '0', '6', 'F', 'c', 'i', 'S', 'P', 'L', 'A', 'I', 'l', 'B', 'R', 'N', 's', 'v', '1', 'X']
Key3 =       ['S', 'C', 'Q', 'x', 'H', 'G', 'e', 'a', 'y', '4', '9', 'p', 'l', '2', 'X', 'R', 'v', 'K', 'f', '3', 'F', 'c', 'U', 'q', 'o', 'V', 'T', '8', 'L', 'n', 'd', 'D', 'W', 'J', 'I', '1', 'N', 'Y', 'M', 'r', ',', ' ', 'O', 'm', '5', '?', 't', 'P', 'z', '7', 'B', 'k', 'i', 'E', 'g', '!', 'j', 'A', '0', 'w', 's', '.', 'Z', '6', 'u', 'h', 'b']

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
            try:
                charpos = Characters.index(str(S1[A]))
                S1[A] = Key[charpos]
                A += 1
            except ValueError:
                S1[A] = S1[A]
                A += 1
        while B < len(S2):
            try:
                charpos2 = Characters.index(str(S2[B]))
                S2[B] = Key2[charpos2]
                B += 1     
            except ValueError:
                S2[B] = S2[B]
                B += 1
        while C < len(S3):
            try:
                charpos3 = Characters.index(str(S3[C]))
                S3[C] = Key3[charpos3]
                C += 1
            except ValueError:
                S3[C] = S3[C]
                C += 1

    if choice == "2":
            
        while A < len(S1):
            try:
                charpos = Key.index(str(S1[A]))
                S1[A] = Characters[charpos]
                A += 1
            except ValueError:
                S1[A] = S1[A]
                A += 1
        while B < len(S2):
            try:
                charpos2 = Key2.index(str(S2[B]))
                S2[B] = Characters[charpos2]
                B += 1
            except ValueError:
                S2[B] = S2[B]
                B += 1
        while C < len(S3):
            try:
                charpos3 = Key3.index(str(S3[C]))
                S3[C] = Characters[charpos3]
                C += 1
            except ValueError:
                S3[C] = S3[C]
                C += 1
                                
    print(*S1, *S2, *S3, sep='')
