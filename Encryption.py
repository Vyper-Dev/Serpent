run = True

#e x a m p l e
#_ _ _ _ _ _ _ _
#0 1 2 3 4 5 6 7
#No Special Chars or Capital Letters

while run == True:
    print("------------")
    print("1.Encrypt\n2.Decrypt")
    choice = input("")
    print("Enter your message:")
    
    def Key1():
        if S1[i] == 'a':
            S1[i] = '-'
        if S1[i] == 'b':
            S1[i] = '!'
        if S1[i] == 'c':
            S1[i] = '['
        if S1[i] == 'd':
            S1[i] = ':'
        if S1[i] == 'e':
            S1[i] = '3'
        if S1[i] == 'f':
            S1[i] = ';'
        if S1[i] == 'g':
            S1[i] = ')'
        if S1[i] == 'h':
            S1[i] = '$'
        if S1[i] == 'i':
            S1[i] = '8'
        if S1[i] == 'j':
            S1[i] = '&'
        if S1[i] == 'k':
            S1[i] = '@'
        if S1[i] == 'l':
            S1[i] = '"'
        if S1[i] == 'm':
            S1[i] = '}'
        if S1[i] == "n":
            S1[i] = '{'
        if S1[i] == 'o':
            S1[i] = '9'
        if S1[i] == 'p':
            S1[i] = '0'
        if S1[i] == 'q':
            S1[i] = '1'
        if S1[i] == 'r':
            S1[i] = '4'
        if S1[i] == 's':
            S1[i] = '/'
        if S1[i] == 't':
            S1[i] = '5'
        if S1[i] == 'u':
            S1[i] = '_'
        if S1[i] == 'v':
            S1[i] = '?'
        if S1[i] == 'w':
            S1[i] = '2'
        if S1[i] == 'x':
            S1[i] = ','
        if S1[i] == 'y':
            S1[i] = '7'
        if S1[i] == 'z':
            S1[i] = ']'
        if S1[i] == ' ':
            S1[i] = '|'
            
    def Key2():
        if S2[i] == 'a':
            S2[i] = '#'
        if S2[i] == 'b':
            S2[i] = '_'
        if S2[i] == 'c':
            S2[i] = '{'
        if S2[i] == 'd':
            S2[i] = ';'
        if S2[i] == 'e':
            S2[i] = '+'
        if S2[i] == 'f':
            S2[i] = '='
        if S2[i] == 'g':
            S2[i] = '|'
        if S2[i] == 'h':
            S2[i] = '('
        if S2[i] == 'i':
            S2[i] = '%'
        if S2[i] == 'j':
            S2[i] = '*'
        if S2[i] == 'k':
            S2[i] = '!'
        if S2[i] == 'l':
            S2[i] = '6'
        if S2[i] == 'm':
            S2[i] = '?'
        if S2[i] == "n":
            S2[i] = '@'
        if S2[i] == 'o':
            S2[i] = '}'
        if S2[i] == 'p':
            S2[i] = '$'
        if S2[i] == 'q':
            S2[i] = '>'
        if S2[i] == 'r':
            S2[i] = '9'
        if S2[i] == 's':
            S2[i] = '1'
        if S2[i] == 't':
            S2[i] = ':'
        if S2[i] == 'u':
            S2[i] = '/'
        if S2[i] == 'v':
            S2[i] = '<'
        if S2[i] == 'w':
            S2[i] = '4'
        if S2[i] == 'x':
            S2[i] = '.'
        if S2[i] == 'y':
            S2[i] = '5'
        if S2[i] == 'z':
            S2[i] = ','
        if S2[i] == ' ':
            S2[i] = ')'
            
    def Key3():
        if S3[i] == 'a':
            S3[i] = '"'
        if S3[i] == 'b':
            S3[i] = '3'
        if S3[i] == 'c':
            S3[i] = '|'
        if S3[i] == 'd':
            S3[i] = '5'
        if S3[i] == 'e':
            S3[i] = ';'
        if S3[i] == 'f':
            S3[i] = '0'
        if S3[i] == 'g':
            S3[i] = '4'
        if S3[i] == 'h':
            S3[i] = '}'
        if S3[i] == 'i':
            S3[i] = '$'
        if S3[i] == 'j':
            S3[i] = '!'
        if S3[i] == 'k':
            S3[i] = '/'
        if S3[i] == 'l':
            S3[i] = '&'
        if S3[i] == 'm':
            S3[i] = ','
        if S3[i] == "n":
            S3[i] = '<'
        if S3[i] == 'o':
            S3[i] = '('
        if S3[i] == 'p':
            S3[i] = ')'
        if S3[i] == 'q':
            S3[i] = '@'
        if S3[i] == 'r':
            S3[i] = '['
        if S3[i] == 's':
            S3[i] = '%'
        if S3[i] == 't':
            S3[i] = '.'
        if S3[i] == 'u':
            S3[i] = ']'
        if S3[i] == 'v':
            S3[i] = '+'
        if S3[i] == 'w':
            S3[i] = '#'
        if S3[i] == 'x':
            S3[i] = '{'
        if S3[i] == 'y':
            S3[i] = '*'
        if S3[i] == 'z':
            S3[i] = '_'
        if S3[i] == ' ':
            S3[i] = '>'
    
    def Solve1():
        if S1[i] == '-':
            S1[i] = 'a'
        if S1[i] == '!':
            S1[i] = 'b'
        if S1[i] == '[':
            S1[i] = 'c'
        if S1[i] == ':':
            S1[i] = 'd'
        if S1[i] == '3':
            S1[i] = 'e'
        if S1[i] == ';':
            S1[i] = 'f'
        if S1[i] == ')':
            S1[i] = 'g'
        if S1[i] == '$':
            S1[i] = 'h'
        if S1[i] == '8':
            S1[i] = 'i'
        if S1[i] == '&':
            S1[i] = 'j'
        if S1[i] == '@':
            S1[i] = 'k'
        if S1[i] == '"':
            S1[i] = 'l'
        if S1[i] == '}':
            S1[i] = 'm'
        if S1[i] == '{':
            S1[i] = 'n'
        if S1[i] == '9':
            S1[i] = 'o'
        if S1[i] == '0':
            S1[i] = 'p'
        if S1[i] == '1':
            S1[i] = 'q'
        if S1[i] == '4':
            S1[i] = 'r'
        if S1[i] == '/':
            S1[i] = 's'
        if S1[i] == '5':
            S1[i] = 't'
        if S1[i] == '_':
            S1[i] = 'u'
        if S1[i] == '?':
            S1[i] = 'v'
        if S1[i] == '2':
            S1[i] = 'w'
        if S1[i] == ',':
            S1[i] = 'x'
        if S1[i] == '7':
            S1[i] = 'y'
        if S1[i] == ']':
            S1[i] = 'z'
        if S1[i] == '|':
            S1[i] = ' '
            
    def Solve2():
        if S2[i] == '#':
            S2[i] = 'a'
        if S2[i] == '_':
            S2[i] = 'b'
        if S2[i] == '{':
            S2[i] = 'c'
        if S2[i] == ';':
            S2[i] = 'd'
        if S2[i] == '+':
            S2[i] = 'e'
        if S2[i] == '=':
            S2[i] = 'f'
        if S2[i] == '|':
            S2[i] = 'g'
        if S2[i] == '(':
            S2[i] = 'h'
        if S2[i] == '%':
            S2[i] = 'i'
        if S2[i] == '*':
            S2[i] = 'j'
        if S2[i] == '!':
            S2[i] = 'k'
        if S2[i] == '6':
            S2[i] = 'l'
        if S2[i] == '?':
            S2[i] = 'm'
        if S2[i] == '@':
            S2[i] = 'n'
        if S2[i] == '}':
            S2[i] = 'o'
        if S2[i] == '$':
            S2[i] = 'p'
        if S2[i] == '>':
            S2[i] = 'q'
        if S2[i] == '9':
            S2[i] = 'r'
        if S2[i] == '1':
            S2[i] = 's'
        if S2[i] == ':':
            S2[i] = 't'
        if S2[i] == '/':
            S2[i] = 'u'
        if S2[i] == '<':
            S2[i] = 'v'
        if S2[i] == '4':
            S2[i] = 'w'
        if S2[i] == '.':
            S2[i] = 'x'
        if S2[i] == '5':
            S2[i] = 'y'
        if S2[i] == ',':
            S2[i] = 'z'
        if S2[i] == ')':
            S2[i] = ' '
            
    def Solve3():
        if S3[i] == '"':
            S3[i] = 'a'
        if S3[i] == '3':
            S3[i] = 'b'
        if S3[i] == '|':
            S3[i] = 'c'
        if S3[i] == '5':
            S3[i] = 'd'
        if S3[i] == ';':
            S3[i] = 'e'
        if S3[i] == '0':
            S3[i] = 'f'
        if S3[i] == '4':
            S3[i] = 'g'
        if S3[i] == '}':
            S3[i] = 'h'
        if S3[i] == '$':
            S3[i] = 'i'
        if S3[i] == '!':
            S3[i] = 'j'
        if S3[i] == '/':
            S3[i] = 'k'
        if S3[i] == '&':
            S3[i] = 'l'
        if S3[i] == ',':
            S3[i] = 'm'
        if S3[i] == '<':
            S3[i] = 'n'
        if S3[i] == '(':
            S3[i] = 'o'
        if S3[i] == ')':
            S3[i] = 'p'
        if S3[i] == '@':
            S3[i] = 'q'
        if S3[i] == '[':
            S3[i] = 'r'
        if S3[i] == '%':
            S3[i] = 's'
        if S3[i] == '.':
            S3[i] = 't'
        if S3[i] == ']':
            S3[i] = 'u'
        if S3[i] == '+':
            S3[i] = 'v'
        if S3[i] == '#':
            S3[i] = 'w'
        if S3[i] == '{':
            S3[i] = 'x'
        if S3[i] == '*':
            S3[i] = 'y'
        if S3[i] == '_':
            S3[i] = 'z'
        if S3[i] == '>':
            S3[i] = ' '
            
            
    if choice == "1":
        Run = True
        i = 0
        ec = list(input(""))
        
        String_Length = len(ec)
        Section_Length = String_Length / 3
        Start = 0
        Stop = int(Section_Length)
        Section_Length = int(Section_Length)
        Start = int(Start)
        Stop = int(Stop)
        
        #print(Start)
        #print(Stop)
        
        S1 = ec[Start : Stop]
        Start = Start + Section_Length
        Stop = Stop + Stop
        
        S2 = ec[Start:Stop]
        Start = Start + Section_Length
        Stop = Stop + Stop
        
        S3 = ec[Start:len(ec)]
        Start = Start + Section_Length
        Stop = Stop + Stop
        
        #print(S1, S2, S3)
            
        while i < len(S1):
            Key1()
            i += 1
            if i == len(S1):
                #print(*S1, sep='')
                i = 0
                break
        while i < len(S2):
            Key2()
            i += 1
            if i == len(S2):
                #print(*S2, sep='')
                i = 0
                break
        while i < len(S3):
            Key3()
            i += 1
            if i == len(S3):
                #print(*S3, sep='')
                i = 0
                break
        print(*S1, *S2, *S3, sep='')
    
    
    if choice == "2":
        Run = True
        i = 0
        dc = list(input(""))
        
        String_Length = len(dc)
        Section_Length = String_Length / 3
        Start = 0
        Stop = int(Section_Length)
        Section_Length = int(Section_Length)
        Start = int(Start)
        Stop = int(Stop)
        
        #print(Start)
        #print(Stop)
        
        S1 = dc[Start : Stop]
        Start = Start + Section_Length
        Stop = Stop + Stop
        
        S2 = dc[Start:Stop]
        Start = Start + Section_Length
        Stop = Stop + Stop
        
        S3 = dc[Start:len(dc)]
        Start = Start + Section_Length
        Stop = Stop + Stop
        
        while i < len(S1):
            Solve1()
            i += 1
            if i == len(S1):
                #print(*S1, sep='')
                i = 0
                break
        while i < len(S2):
            Solve2()
            i += 1
            if i == len(S2):
                #print(*S2, sep='')
                i = 0
                break
        while i < len(S3):
            Solve3()
            i += 1
            if i == len(S3):
                #print(*S3, sep='')
                i = 0
                break
        print(*S1, *S2, *S3, sep='')
                
                
    if choice == "quit":
        break