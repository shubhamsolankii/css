def encryptRailFence(plainText, railKey):
    railMatrix = [['\n' for _ in range(len(plainText))] for _ in range(railKey)]
    directionDown = False
    currentRow, currentColumn = 0, 0
    for charIndex in range(len(plainText)):
        if (currentRow == 0) or (currentRow == railKey - 1):
            directionDown = not directionDown
        railMatrix[currentRow][currentColumn] = plainText[charIndex]
        currentColumn += 1
        if directionDown:
            currentRow += 1
        else:
            currentRow -= 1
    encryptedTextList = []
    for rowIndex in range(railKey):
        for colIndex in range(len(plainText)):
            if railMatrix[rowIndex][colIndex] != '\n':
                encryptedTextList.append(railMatrix[rowIndex][colIndex])
    return "".join(encryptedTextList)

def decryptRailFence(cipherText, railKey):
    railMatrix = [['\n' for _ in range(len(cipherText))] for _ in range(railKey)]
    directionDown = None
    currentRow, currentColumn = 0, 0
    for charIndex in range(len(cipherText)):
        if currentRow == 0:
            directionDown = True
        if currentRow == railKey - 1:
            directionDown = False
        railMatrix[currentRow][currentColumn] = '*'
        currentColumn += 1
        if directionDown:
            currentRow += 1
        else:
            currentRow -= 1
    cipherIndex = 0
    for rowIndex in range(railKey):
        for colIndex in range(len(cipherText)):
            if railMatrix[rowIndex][colIndex] == '*' and cipherIndex < len(cipherText):
                railMatrix[rowIndex][colIndex] = cipherText[cipherIndex]
                cipherIndex += 1
    decryptedTextList = []
    currentRow, currentColumn = 0, 0
    for charIndex in range(len(cipherText)):
        if currentRow == 0:
            directionDown = True
        if currentRow == railKey - 1:
            directionDown = False
        if railMatrix[currentRow][currentColumn] != '*':
            decryptedTextList.append(railMatrix[currentRow][currentColumn])
            currentColumn += 1
        if directionDown:
            currentRow += 1
        else:
            currentRow -= 1
    return "".join(decryptedTextList)

userChoice = int(input("What do you want to do?\n1. Encrypt\n2. Decrypt\nYour choice: "))
if userChoice == 1:
    with open("plain-text.txt", "r") as inputFile:
        railKey = int(inputFile.readline().strip())
        plainText = inputFile.readline().strip()

    encryptedText = encryptRailFence(plainText, railKey)
    resultText = str(railKey) + "\n" + encryptedText
    
    with open("cipher-text.txt", "w") as outputFile:
        outputFile.write(resultText)

    print("Encryption completed successfully.", '\n')
    print("Encrypted text: ", encryptedText)
elif userChoice == 2:
    with open("cipher-text.txt", "r") as inputFile:
        railKey = int(inputFile.readline().strip())
        cipherText = inputFile.readline().strip()

    decryptedText = decryptRailFence(cipherText, railKey)
    resultText = str(railKey) + "\n" + decryptedText

    with open("outplain-text.txt", "w") as outputFile:
        outputFile.write(resultText)

    print("Decryption completed successfully.", '\n')
    print("Decrypted text: ", decryptedText)
else:
    print("Invalid choice!")
