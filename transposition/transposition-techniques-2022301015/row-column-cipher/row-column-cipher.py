import math

def encryptMessageByRowColumn(message, key):
    cipherText = ""
    keyIndex = 0
    messageLength = float(len(message))
    messageList = list(message)
    sortedKeyList = sorted(list(key))
    numberOfColumns = len(key)
    numberOfRows = int(math.ceil(messageLength / numberOfColumns))
    fillNullCharacters = int((numberOfRows * numberOfColumns) - messageLength)
    messageList.extend('_' * fillNullCharacters)
    matrix = [messageList[i: i + numberOfColumns] for i in range(0, len(messageList), numberOfColumns)]
    for _ in range(numberOfColumns):
        currentIndex = key.index(sortedKeyList[keyIndex])
        cipherText += ''.join([row[currentIndex] for row in matrix])
        keyIndex += 1
    return cipherText

def decryptMessageByRowColumn(cipherText, key):
    decryptedMessage = ""
    keyIndex = 0
    messageIndex = 0
    cipherLength = float(len(cipherText))
    cipherList = list(cipherText)
    numberOfColumns = len(key)
    numberOfRows = int(math.ceil(cipherLength / numberOfColumns))
    sortedKeyList = sorted(list(key))
    decryptedMatrix = []
    for _ in range(numberOfRows):
        decryptedMatrix.append([None] * numberOfColumns)
    for _ in range(numberOfColumns):
        currentIndex = key.index(sortedKeyList[keyIndex])
        for rowIndex in range(numberOfRows):
            decryptedMatrix[rowIndex][currentIndex] = cipherList[messageIndex]
            messageIndex += 1
        keyIndex += 1
    try:
        decryptedMessage = ''.join(sum(decryptedMatrix, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
    nullCharacterCount = decryptedMessage.count('_')
    if nullCharacterCount > 0:
        return decryptedMessage[:-nullCharacterCount]
    return decryptedMessage

userChoice = int(input("What do you want to do?\n1. Encrypt\n2. Decrypt\nYour choice: "))
if userChoice == 1:
    with open("plain-text.txt", "r") as inputFile:
        key = inputFile.readline().strip()
        text = inputFile.readline().strip()

    encryptedResult = encryptMessageByRowColumn(text, key)
    result = key + "\n" + encryptedResult
    
    with open("cipher-text.txt", "w") as outputFile:
        outputFile.write(result)

    print("Encryption completed successfully.", '\n')
    print("Encrypted text: ", encryptedResult)
elif userChoice == 2:
    with open("cipher-text.txt", "r") as inputFile:
        key = inputFile.readline().strip()
        text = inputFile.readline().strip()

    decryptedResult = decryptMessageByRowColumn(text, key)
    result = key + "\n" + decryptedResult

    with open("outplain-text.txt", "w") as outputFile:
        outputFile.write(result)

    print("Decryption completed successfully.", '\n')
    print("Decrypted text: ", decryptedResult)
else:
    print("Invalid choice!")
