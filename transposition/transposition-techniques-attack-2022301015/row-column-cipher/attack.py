import itertools
import math

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
            if messageIndex < len(cipherList):
                decryptedMatrix[rowIndex][currentIndex] = cipherList[messageIndex]
                messageIndex += 1
        keyIndex += 1
    
    decryptedMessage = ''.join([char for row in decryptedMatrix for char in row if char is not None])
    
    nullCharacterCount = decryptedMessage.count('_')
    
    if nullCharacterCount > 0:
        return decryptedMessage[:-nullCharacterCount]
    
    return decryptedMessage

def attackRowColumn(cipherText):
    attackResults = []
    numberOfColumns = math.ceil(math.sqrt(len(cipherText)))
    
    for length in range(2, numberOfColumns + 2):
        keyPermutations = itertools.permutations(''.join(str(i) for i in range(1, length + 1)))
        
        for keyPermutation in keyPermutations:
            keyString = ''.join(keyPermutation)
            decryptedText = decryptMessageByRowColumn(cipherText, keyString)
            attackResults.append(f"Key: {keyString}\nDecrypted Text: {decryptedText}\n\n")
    
    return attackResults

with open("cipher-text.txt", "r") as inputFile:
    cipherText = inputFile.readline().strip()

attackResults = attackRowColumn(cipherText)

with open("attack-results.txt", "w") as outputFile:
    outputFile.writelines(attackResults)

print("Attack completed successfully.")
