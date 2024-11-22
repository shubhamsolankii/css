import string

def cleanKey(encryptionKey):
    return ''.join(filter(str.isalpha, encryptionKey)).lower()

def createCipherAlphabet(encryptionKey):
    standardAlphabet = string.ascii_lowercase
    cleanedKey = cleanKey(encryptionKey)
    cleanedKey = ''.join(sorted(set(cleanedKey), key=cleanedKey.index))
    remainingLetters = ''.join([char for char in standardAlphabet if char not in cleanedKey])
    cipherAlphabet = cleanedKey + remainingLetters
    return cipherAlphabet

def encryptText(plainText, encryptionKey):
    standardAlphabet = string.ascii_lowercase
    cipherAlphabet = createCipherAlphabet(encryptionKey)
    translationTable = str.maketrans(standardAlphabet, cipherAlphabet)
    return plainText.lower().translate(translationTable)

def decryptText(cipherText, decryptionKey):
    standardAlphabet = string.ascii_lowercase
    cipherAlphabet = createCipherAlphabet(decryptionKey)
    translationTable = str.maketrans(cipherAlphabet, standardAlphabet)
    return cipherText.lower().translate(translationTable)

userChoice = int(input("Select the operation you want to perform. \n\n1. Encrypt\n2. Decrypt\n\nYour choice: "))
if userChoice == 1:
    with open("plain-text.txt", "r") as inputFile:
        encryptionKey = inputFile.readline().strip()
        plainText = inputFile.readline().strip()
    
    resultText = encryptionKey + "\n" + encryptText(plainText, encryptionKey)
    
    with open("cipher-text.txt", "w") as outputFile:
        outputFile.write(resultText)

    print("Encryption completed successfully.")
elif userChoice == 2:
    with open("cipher-text.txt", "r") as inputFile:
        decryptionKey = inputFile.readline().strip()
        cipherText = inputFile.readline().strip()
    
    resultText = decryptionKey + "\n" + decryptText(cipherText, decryptionKey)

    with open("outplain-text.txt", "w") as outputFile:
        outputFile.write(resultText)

    print("Decryption completed successfully.")
else:
    print("Invalid choice!")