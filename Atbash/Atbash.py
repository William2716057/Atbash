while True:
    plaintext = input("Enter Message to encrypt or decrypt: ").upper()

    ciphertext = ""
    for letter in plaintext:
        ascii = ord(letter)
        # keep between A and Z ascii
        if ascii >= 65 and ascii <= 90:
            # subtract 65 from ascii representation of letter
            position = ascii - 65
            # apply Atbash formula
            NewPos = 25 - position
            newAscii = NewPos + 65
            # chr returns an ascii value as character
            NewLetter = chr(newAscii)
        else:
            NewLetter = letter
        ciphertext = ciphertext + NewLetter
    print("Encrypted/Decrypted Message:", ciphertext)

    repeat = input("Do you want to encrypt or decrypt another message? (yes/no): ").lower()
    if repeat == 'yes' or repeat == 'y':
        continue
    elif repeat == 'no' or repeat == 'n':
        break
    else:
        print("Please enter in form of 'yes', 'no', 'y' or 'n'.")