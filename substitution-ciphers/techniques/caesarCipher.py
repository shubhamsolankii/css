def caesarCipher(inputString, shiftKey):
    resultString = ""
    for character in inputString:
        if not character.isalpha():
            resultString += character
        else:
            if character.isupper():
                resultString += chr((ord(character) + shiftKey - 65) % 26 + 65)
            else:
                resultString += chr((ord(character) + shiftKey - 97) % 26 + 97)
    return resultString

userChoice = int(input("Select the operation you want to perform. \n\n1. Encrypt\n2. Decrypt\n\nYour choice: "))

if userChoice == 1:
    with open("plain-text.txt", "r") as inputFile:
        key = inputFile.readline().strip()
        plainText = inputFile.readline().strip()
    
    cipherKey = int(key) % 26
    resultString = key + "\n" + caesarCipher(plainText, cipherKey)
    
    with open("cipher-text.txt", "w") as outputFile:
        outputFile.write(resultString)

    print("Encryption completed successfully.")
elif userChoice == 2:
    with open("cipher-text.txt", "r") as inputFile:
        key = inputFile.readline().strip()
        cipherText = inputFile.readline().strip()
    
    cipherKey = int(key) % 26
    resultString = key + "\n" + caesarCipher(cipherText, 26 - cipherKey)

    with open("outplain-text.txt", "w") as outputFile:
        outputFile.write(resultString)

    print("Decryption completed successfully.")
else:
    print("Invalid choice!")
