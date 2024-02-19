
#encrypt one letter at a time
#letter = "A"

plaintext = "message".upper()
for letter in plaintext:
    ascii = ord(letter)
    #keep between A and Z ascii
    if ascii>=65 and ascii<=90:
    #print(ascii)
    #subtract 65 from ascii representation of letter
        position = ascii - 65
        #print(position)

        #apply Atbash formula 
        NewPos = 25 - position 
        #print(NewPos)

        newAscii = NewPos + 65
        #chr returns an ascii value as character
        NewLetter =chr(newAscii)
        #print(NewLetter)
    else:
        NewLetter = letter
    print(NewLetter)