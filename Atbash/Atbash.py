
#encrypt one letter at a time
#letter = "A"

plaintext = "message"
for letter in plaintext:
    ascii = ord(letter)
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
    print(NewLetter)