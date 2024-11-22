from collections import Counter

def performFrequencyAnalysis(cipherText):
    frequencyCounts = Counter(cipherText)
    totalCount = sum(frequencyCounts.values())
    frequencyPercentages = {character: (count / totalCount) * 100 for character, count in frequencyCounts.items()}
    return frequencyPercentages

def executePolyalphabeticAttack(inputFilePath, outputFilePath):
    with open(inputFilePath, 'r') as inputFile:
        cipherText = inputFile.read().strip()  # Read the ciphertext from the file

    frequencyPercentages = performFrequencyAnalysis(cipherText)

    with open(outputFilePath, 'w') as outputFile:
        for character, percentage in sorted(frequencyPercentages.items()):
            outputFile.write(f"{character}: {percentage:.2f}%\n")

# File paths
inputFilePath = 'cipher-text.txt'
outputFilePath = 'attackResults.txt'

executePolyalphabeticAttack(inputFilePath, outputFilePath)
