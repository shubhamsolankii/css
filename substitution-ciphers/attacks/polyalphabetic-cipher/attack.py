from collections import Counter
import string

def performFrequencyAnalysis(cipherText):
    frequencyCounts = Counter(cipherText)
    totalCount = sum(frequencyCounts.values())
    frequencyPercentages = {character: (count / totalCount) * 100 for character, count in frequencyCounts.items()}
    return frequencyPercentages

def executePolyalphabeticAttack(inputFilePath, outputFilePath):
    with open(inputFilePath, 'r') as inputFile:
        cipherText = inputFile.read().strip()

    frequencyPercentages = performFrequencyAnalysis(cipherText)

    with open(outputFilePath, 'w') as outputFile:
        for character, percentage in frequencyPercentages.items():
            outputFile.write(f"{character}: {percentage:.2f}%\n")

    print("Polyalphabetic attack completed successfully.")

if __name__ == "__main__":
    inputFilePath = 'cipher-text.txt'
    outputFilePath = 'attackResults.txt'
    
    executePolyalphabeticAttack(inputFilePath, outputFilePath)
