from collections import Counter

englishLetterFrequencies = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33,
    'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41,
    'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98,
    'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07
}

def performFrequencyAnalysis(cipherText):
    cipherTextFrequencies = Counter(cipherText)

    sortedCipherTextFrequencies = sorted(cipherTextFrequencies.items(), key=lambda item: item[1], reverse=True)
    
    sortedEnglishLetterFrequencies = sorted(englishLetterFrequencies.items(), key=lambda item: item[1], reverse=True)

    frequencyMapping = {}
    for i in range(len(sortedCipherTextFrequencies)):
        cipherLetter = sortedCipherTextFrequencies[i][0]
        englishLetter = sortedEnglishLetterFrequencies[i][0]
        frequencyMapping[cipherLetter] = englishLetter

    decryptedPlaintext = ''.join([frequencyMapping.get(character, character) for character in cipherText])
    
    return decryptedPlaintext, frequencyMapping

def main():
    inputFilePath = 'cipher-text.txt'
    outputFilePath = 'attackResults.txt'

    with open(inputFilePath, 'r') as inputFile:
        cipherText = inputFile.read().strip()

    decryptedText, letterMapping = performFrequencyAnalysis(cipherText)
    
    with open(outputFilePath, 'w') as outputFile:
        outputFile.write("Decrypted Text: " + decryptedText + "\n")
        outputFile.write("Letter Mapping: " + str(letterMapping) + "\n")

    print("Frequency analysis completed successfully.")

if __name__ == "__main__":
    main()
