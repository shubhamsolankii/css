from collections import Counter
import string
import matplotlib.pyplot as plt

def plotCharacterFrequencies(plainText, cipherTexts, cipherLabels):
    def calculateNormalizedFrequencies(text):
        text = text.lower()
        text = ''.join(filter(lambda char: char in string.ascii_lowercase, text))
        frequencyCounter = Counter(text)
        maxFrequency = max(frequencyCounter.values(), default=1)
        normalizedFrequency = {char: (count / maxFrequency) * 100 for char, count in frequencyCounter.items()}
        return normalizedFrequency

    plainTextFrequencies = calculateNormalizedFrequencies(plainText)

    sortedLetters = sorted(plainTextFrequencies.items(), key=lambda item: item[1], reverse=True)
    xLabels = [char for char, _ in sortedLetters]

    def prepareFrequencyData(frequencyData):
        sortedFrequencyData = sorted(frequencyData.items(), key=lambda item: item[1], reverse=True)
        sortedCharacters = [char for char, _ in sortedFrequencyData]
        sortedCounts = [count for _, count in sortedFrequencyData]
        return sortedCharacters, sortedCounts

    plainTextCharacters, plainTextCounts = prepareFrequencyData(plainTextFrequencies)

    for i, cipherText in enumerate(cipherTexts):
        fig, axis = plt.subplots(figsize=(12, 8))

        cipherTextFrequencies = calculateNormalizedFrequencies(cipherText)
        cipherTextCharacters, cipherTextCounts = prepareFrequencyData(cipherTextFrequencies)
        axis.plot(range(len(cipherTextCharacters)), cipherTextCounts, label=cipherLabels[i], marker='o', linestyle='-', color=plt.cm.tab10(i))

        axis.set_title(f'Normalized Character Frequency Comparison for {cipherLabels[i]}')
        axis.set_xlabel('Frequency Rank')
        axis.set_ylabel('Frequency (%)')
        axis.legend()
        axis.grid(True)

        axis.set_xticks(range(len(xLabels)))
        axis.set_xticklabels(xLabels, rotation=90)

        plt.show()

with open("plain-text.txt", "r") as file:
    plainText = file.readline().strip()

cipherTexts = []
with open("cipher-text.txt", "r") as file:
    for line in file:
        cipherTexts.append(line.strip())

cipherLabels = [
    "Rail Fence Cipher",
    "Row Column Transposition Cipher",
    "Double Row Column Transposition Cipher"
]

plotCharacterFrequencies(plainText, cipherTexts, cipherLabels)