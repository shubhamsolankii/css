import re

class PlayfairCipher:
    def __init__(self):
        self.matrixSize = 5

    def generateKeyMatrix(self, key):
        matrix = [['-'] * self.matrixSize for _ in range(self.matrixSize)]
        charSet = set()
        index = 0

        for char in key.upper():
            if char not in charSet:
                charSet.add(char)
                matrix[index // self.matrixSize][index % self.matrixSize] = char
                index += 1

        for i in range(26):
            char = chr(i + 65)
            if char == 'J':
                continue
            if char not in charSet:
                charSet.add(char)
                matrix[index // self.matrixSize][index % self.matrixSize] = char
                index += 1

        return matrix

    def createDigrams(self, text):
        digrams = []
        index = 0
        text = re.sub(r'\s+', '', text)
        text = text.replace('J', 'I')
        while index < len(text):
            if index == len(text) - 1:
                digrams.append(text[index] + 'X')
                break
            if text[index] == text[index + 1]:
                digrams.append(text[index] + 'X')
                index += 1
            else:
                digrams.append(text[index] + text[index + 1])
                index += 2
        return digrams

    def getCoordinates(self, char, matrix):
        if char == 'J':
            char = 'I'

        for row in range(self.matrixSize):
            for column in range(self.matrixSize):
                if char == matrix[row][column]:
                    return row, column

        return -1, -1

    def substitute(self, firstChar, secondChar, matrix, isCipher=True):
        offset = 1 if isCipher else -1
        firstCharCoordinates = self.getCoordinates(firstChar, matrix)
        secondCharCoordinates = self.getCoordinates(secondChar, matrix)

        if firstCharCoordinates[0] == secondCharCoordinates[0]:
            row = firstCharCoordinates[0]
            return matrix[row][(firstCharCoordinates[1] + offset) % self.matrixSize], matrix[row][(secondCharCoordinates[1] + offset) % self.matrixSize]
        elif firstCharCoordinates[1] == secondCharCoordinates[1]:
            column = firstCharCoordinates[1]
            return matrix[(firstCharCoordinates[0] + offset) % self.matrixSize][column], matrix[(secondCharCoordinates[0] + offset) % self.matrixSize][column]
        else:
            return matrix[firstCharCoordinates[0]][secondCharCoordinates[1]], matrix[secondCharCoordinates[0]][firstCharCoordinates[1]]

    def playfairEncrypt(self, digrams, matrix):
        cipherText = ""
        for digram in digrams:
            firstChar, secondChar = self.substitute(digram[0], digram[1], matrix)
            cipherText += firstChar + secondChar
        return cipherText

    def playfairDecrypt(self, digrams, matrix):
        decipheredText = ""
        for digram in digrams:
            firstChar, secondChar = self.substitute(digram[0], digram[1], matrix, isCipher=False)
            decipheredText += firstChar + secondChar
        return decipheredText

# Input and output file handling
userChoice = int(input("What do you want to do?\n1. Encrypt\n2. Decrypt\nYour choice: "))

cipher = PlayfairCipher()

if userChoice == 1:
    with open('plain-text.txt') as file:
        lines = file.readlines()
        key = lines[0].strip()
        text = lines[1].strip()
        plaintext = "".join([char for char in text if 'A' <= char <= 'Z'])
    
    keyMatrix = cipher.generateKeyMatrix(key)
    
    print("Key Matrix: ")
    for row in keyMatrix:
        print(row)
    print()

    digrams = cipher.createDigrams(plaintext)
    print("Digrams generated")
    print(digrams)
    print()

    encryptedText = cipher.playfairEncrypt(digrams, keyMatrix)
    print("Generated Cipher text:")
    print(encryptedText)
    print()

    print("Writing ciphertext to file...")
    with open('cipher-text.txt', 'w') as cipherFile:
        cipherFile.write(key + '\n')
        cipherFile.write(encryptedText)
    print("Encryption completed successfully.")
    print()

elif userChoice == 2:
    with open('cipher-text.txt') as file:
        lines = file.readlines()
        key = lines[0].strip()
        encryptedText = lines[1].strip()
    
    keyMatrix = cipher.generateKeyMatrix(key)

    digrams = cipher.createDigrams(encryptedText)
    print("Digrams from ciphertext")
    print(digrams)
    print()

    decryptedText = cipher.playfairDecrypt(digrams, keyMatrix)
    print("Deciphered text:")
    print(decryptedText)
    print()

    print("Writing decrypted text to file...")
    with open('outplain-text.txt', 'w') as outputFile:
        outputFile.write(key + '\n')
        outputFile.write(decryptedText)
    print("Decryption completed successfully.")
else:
    print("Invalid choice!")
