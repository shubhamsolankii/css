def generateKey(plainText, encryptionKey):
    encryptionKeyList = list(encryptionKey)
    if len(plainText) == len(encryptionKeyList):
        return "".join(encryptionKeyList)
    else:
        for i in range(len(plainText) - len(encryptionKeyList)):
            encryptionKeyList.append(encryptionKeyList[i % len(encryptionKeyList)])
    return "".join(encryptionKeyList)

def encryptText(plainText, encryptionKey):
    cipherText = []
    for i in range(len(plainText)):
        x = (ord(plainText[i]) + ord(encryptionKey[i])) % 26
        x += ord('A')
        cipherText.append(chr(x))
    return "".join(cipherText)

def decryptText(cipherText, decryptionKey):
    originalText = []
    for i in range(len(cipherText)):
        x = (ord(cipherText[i]) - ord(decryptionKey[i]) + 26) % 26
        x += ord('A')
        originalText.append(chr(x))
    return "".join(originalText)


if __name__ == "__main__":
    userChoice = int(input("Select the operation you want to perform \n\n1. Encrypt\n2. Decrypt\n\nYour choice: "))

    if userChoice == 1:
        with open("plain-text.txt", "r") as inputFile:
            encryptionKey = inputFile.readline().strip()
            plainText = inputFile.readline().strip()

        generatedKey = generateKey(plainText, encryptionKey)
        encryptedText = encryptText(plainText, generatedKey)

        with open("cipher-text.txt", "w") as outputFile:
            outputFile.write(encryptionKey + "\n" + encryptedText)

        print("Encryption completed successfully.")

    elif userChoice == 2:
        with open("cipher-text.txt", "r") as inputFile:
            decryptionKey = inputFile.readline().strip()
            cipherText = inputFile.readline().strip()

        generatedKey = generateKey(cipherText, decryptionKey)
        decryptedText = decryptText(cipherText, generatedKey)

        with open("outplain-text.txt", "w") as outputFile:
            outputFile.write(decryptionKey + "\n" + decryptedText)

        print("Decryption completed successfully.")

    else:
        print("Invalid choice!")
