import os
import random
import string
import math

def Menu():

    os.system('clear')

    print "Welcome to the RunCMD Cryptology Suite, What would you like to do?\n\n[1] Use Caesar Ciphers\n\n[2] Use Vigenere Cipher\n\n[3] Columnar Transposition\n"

    MenuInput = raw_input()

    if MenuInput == "1":
        Caesar()
    elif MenuInput == "2":
        Vigenere()
    elif MenuInput == "3":
        CShift()

def Caesar():

    os.system('clear')

    print "Would you like to:\n\n[1] Encrypt\n\n[2] Decrypt\n\n[3] Return to Main Menu\n"

    CaesarInput = raw_input()

    if CaesarInput == "1":
        CEncrypt()
    elif CaesarInput == "2":
        CDecrypt()
    elif CaesarInput == "3":
        Menu()
    else:
        CEncrypt()

def CEncrypt():
      
    os.system('clear')

    print "Please enter the text you want to encrypt\n"

    PlainText = raw_input()

    ShiftKey = random.randrange(0, 25)

    os.system('clear')

    print "The Keylength is " + str(ShiftKey) + "\n"

    PlainCharacters = list(PlainText)

    NewChars = []

    for i in PlainCharacters:
        if 0 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or ord(i) > 122:
            NewChars.append(i)
        elif 65 <= ord(i) <= 90:
            if (int(ord(i)) + int(ShiftKey)) > 90:
                NewChars.append(chr(ord(i) + (ShiftKey - 26)))
            else:
                NewChars.append(chr(ord(i) + ShiftKey))
        elif 97 <= ord(i) <= 122:
            if (int(ord(i)) + int(ShiftKey)) > 122:
                NewChars.append(chr(ord(i) + (ShiftKey - 26)))
            else:
                NewChars.append(chr(ord(i) + ShiftKey))

    print "Your Message Encrypted is:\n" + ''.join(NewChars)

    print "\nWould you like to:\n\n[1] Return to the Main Menu\n\n[2] Return to the Caesar Cypher Menu\n"

    CEncryptInput = raw_input()
    
    if CEncryptInput == "1":
        Menu()
    elif CEncryptInput == "2":
        Caesar()
    else:
        Menu()

def CDecrypt():

    os.system('clear')

    print "Please enter the encrypted text\n"

    EncryptedText = raw_input()

    EncryptedCharacters = list(EncryptedText)

    print "\nDo you know the length of the key/shift?\n\n[1] Yes\n\n[2] No\n"

    CDecryptKeyQInput = raw_input()

    if CDecryptKeyQInput == "1":
        print "\nPlease input the key/shift length\n"
        DKey = str(26 - int(raw_input()))
        DecryptedChars = []
        if DKey.isdigit() == True:
            for i in EncryptedCharacters:
                if 0 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or ord(i) > 122:
                    DecryptedChars.append(i)
                elif 65 <= ord(i) <= 90:
                    if (int(ord(i)) + int(DKey)) > 90:
                        DecryptedChars.append(chr(ord(i) - (26 - int(DKey))))
                    else:
                        DecryptedChars.append(chr(ord(i) + (int(DKey))))
                elif 97 <= ord(i) <= 122:
                    if (int(ord(i)) + int(DKey)) > 122:
                        DecryptedChars.append(chr(ord(i) - (26 - int(DKey))))
                    else:
                        DecryptedChars.append(chr(ord(i) + (int(DKey))))
    else:
        for x in range(1, 26):
            os.system('clear')
            DKey = x
            print "\nTested key length " + str(x) + ":\n\n"
            DecryptedChars = []
            for i in EncryptedCharacters:
                if 0 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or ord(i) > 122:
                    DecryptedChars.append(i)
                elif 65 <= ord(i) <= 90:
                    if (int(ord(i)) + int(DKey)) > 90:
                        DecryptedChars.append(chr(ord(i) - (26 - int(DKey))))
                    else:
                        DecryptedChars.append(chr(ord(i) + (int(DKey))))
                elif 97 <= ord(i) <= 122:
                    if (int(ord(i)) + int(DKey)) > 122:
                        DecryptedChars.append(chr(ord(i) - (26 - int(DKey))))
                    else:
                        DecryptedChars.append(chr(ord(i) + (int(DKey))))
            print ''.join(DecryptedChars) + "\n\nDo you think that this is correct?\n\n[1] Yes\n\n[2] No\n"
            DCorrectQ = raw_input()
            if DCorrectQ == "1":
                break         

    os.system('clear')

    print "\nYour message decrypted is:\n" + ''.join(DecryptedChars)

    print "\nWould you like to:\n\n[1] Return to the Main Menu\n\n[2] Return to the Caesar Cypher Menu\n"

    CDecryptInput = raw_input()
    
    if CEncryptInput == "1":
        Menu()
    elif CEncryptInput == "2":
        Caesar()
    else:
        Menu()

def Vigenere():
    
    os.system('clear')

    print "Would you like to:\n\n[1] Encrypt\n\n[2] Decrypt\n\n[3] Return to Main Menu\n"

    VigenereInput = raw_input()

    if VigenereInput == "1":
        VEncrypt()
    elif VigenereInput == "2":
        VDecrypt()
    elif VigenereInput == "3":
        Menu()
    else:
        VEncrypt()

def VEncrypt():

    os.system('clear')
    
    print "Please enter the text you want to encrypt\n"
    
    PlainText = raw_input()
    
    PlainChars = list(PlainText)

def CShift():

    os.system('clear')

    print "Would you like to:\n\n[1] Encrypt\n\n[2] Decrypt\n\n[3] Return to Main Menu\n"

    CShiftInput = raw_input()

    if CShiftInput == "1":
        CSEncrypt()
    elif CShiftInput == "2":
        CSDecrypt()
    elif CShiftInput == "3":
        Menu()
    else:
        CSEncrypt()

def CSEncrypt():

    os.system('clear')

    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    print "Please enter the text you want to encrypt:\n"

    PlainText = raw_input()

    PlainText = PlainText.upper()

    PlainText = PlainText.replace(" ", "")

    PlainChars = list(PlainText)

    TextLength = len(PlainText)

    print "\nPlease input the key length\n"

    KeyLength = raw_input()

    RowNum = int(math.ceil(TextLength / float(KeyLength)))

    Row = []

    for i in range (1, (RowNum + 1)):
        Row.append(PlainText[((i-1)*(int(KeyLength))):(i*(int(KeyLength)))])
        
    Columns = []

    for i in range (int(KeyLength)):
        Columns.append(PlainText[i::int(KeyLength)])

    print "\nWould you like to use a random key or define your own?\n\n[1] Random (More Secure)\n\n[2] User Defined\n"

    KeyDec = raw_input()

    if KeyDec == "1":
        KeyList = []
        for i in range (int(KeyLength)):
            KeyList.append(i)
        random.shuffle(KeyList)
    elif KeyDec == "2":
        KeyList = []
        for i in range (int(KeyLength)):
            os.system('clear')
            print "Please input character " + str(i) + " of your desired key\n"
            KeyList.append(int(raw_input()))

    NewColumns = []

    for i in range(int(KeyLength)):
        NewColumns.append(Columns[KeyList[i]])

    NewRows = []

    TempJoin = ''.join(NewColumns)

    for i in range (int(KeyLength)):
        if len(NewColumns[i]) < RowNum:
            NewColumns[i] = NewColumns[i] + "-"

    for i in range (RowNum):
        NewRows.append("")

    for i in range (RowNum):
        for x in range (int(KeyLength)):
            NewRows[i] = NewRows[i] + NewColumns[x][i]

    EncResult = ''.join(NewRows)

    os.system('clear')
    
    print "Would you like to inject random characters? (This will massively improve effectiveness)\n\n[1] Yes\n\n[2] No\n"

    InjDec = raw_input()

    if InjDec == "1":
        RndList = []
        InsertChars = []
        RndNeeded = int(math.floor(float(TextLength)/2))
        for i in range (RndNeeded):
            RndList.append(random.randrange(0, 25))
            InsertChars.append(Alphabet[RndList[i]])
        Pieces = []
        for i in range (RndNeeded + 1):
            Pieces.append(EncResult[(i * 2):((i * 2) + 2)])
        for i in range (RndNeeded):
            Pieces[i] = Pieces[i] + InsertChars[i]    
        FinalEnc = ''.join(Pieces)
        print "\nYour message encrypted is:\n\n" + FinalEnc + "\n\nWould you like to:\n\n[1] Return to the columnar shift menu\n\n[2] Return to the main menu\n"
    elif InjDec == "2":
        print "\nYour message encrypted is:\n\n" + EncResult + "\n\nWould you like to:\n\n[1] Return to the columnar shift menu\n\n[2] Return to the main menu\n"

    EndDec = raw_input()
    
    if EndDec == 1:
        CShift()
    elif EndDec == 2:
        Menu()
    else:
        Menu()

def CSDecrypt():

    print "Please enter the text to be decrypted:\n"

    EncryptedText = raw_input()

    print "\nDo you know if random characters have been injected?\n\n[1] Yes\n\n[2] No\n"

Menu()
