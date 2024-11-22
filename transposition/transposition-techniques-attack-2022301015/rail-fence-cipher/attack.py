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

def attackRailFence(cipherText):
    attackResults = []
    for railDepth in range(2, len(cipherText) + 1):
        decryptedText = decryptRailFence(cipherText, railDepth)
        attackResults.append(f"Depth {railDepth}:\n{decryptedText}\n\n")
    return attackResults

with open("cipher-text.txt", "r") as inputFile:
    cipherText = inputFile.readline().strip()

attackResults = attackRailFence(cipherText)

with open("attack-results.txt", "w") as outputFile:
    outputFile.writelines(attackResults)

print("Attack completed successfully.")
