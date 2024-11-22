import itertools
import math

def decryptMessageByRowColumn(cipherText, key, level):
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
            if messageIndex < len(cipherList):
                decryptedMatrix[rowIndex][currentIndex] = cipherList[messageIndex]
                messageIndex += 1
        keyIndex += 1
    
    decryptedMessage = ''.join([char for row in decryptedMatrix for char in row if char is not None])
    
    if level == 2:
        return decryptedMessage
    elif level == 1:
        nullCharacterCount = decryptedMessage.count('_')
        if nullCharacterCount > 0:
            return decryptedMessage[:-nullCharacterCount]
    
    return decryptedMessage

def attackDoubleRowColumn(cipherText):
    attackResults = []
    numberOfColumns = math.ceil(math.sqrt(len(cipherText)))
    
    for length in range(2, numberOfColumns + 1):
        keyPermutations = itertools.permutations(''.join(str(i) for i in range(1, length + 1)))
        
        for key in keyPermutations:
            keyString = ''.join(key)
            intermediateText = decryptMessageByRowColumn(cipherText, keyString, 2)
            decryptedText = decryptMessageByRowColumn(intermediateText, keyString, 1)
            attackResults.append(f"Key: {keyString}\nDecrypted Text: {decryptedText}\n\n")
    
    return attackResults

with open("cipher-text.txt", "r") as inputFile:
    cipherText = inputFile.readline().strip()

attackResults = attackDoubleRowColumn(cipherText)

with open("attack-results.txt", "w") as outputFile:
    outputFile.writelines(attackResults)

print("Attack completed successfully.")
