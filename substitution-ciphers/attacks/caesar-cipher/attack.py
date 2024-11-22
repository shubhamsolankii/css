with open("cipher-text.txt", "r") as inputFile:
    secretKey = inputFile.readline().strip()
    cipherText = inputFile.readline().strip()

secretKeyAsInteger = int(secretKey) % 26

with open("attackResults.txt", "w") as outputFile:
    for shiftAmount in range(26):
        decryptedText = ""
        for character in cipherText:
            if not character.isalpha():
                decryptedText += character
            else:
                if character.isupper():
                    decryptedText += chr((ord(character) - shiftAmount - 65) % 26 + 65)
                else:
                    decryptedText += chr((ord(character) - shiftAmount - 97) % 26 + 97)
        decryptedText += "\n\n"
        outputFile.write(decryptedText)

print("Attack completed successfully.")
