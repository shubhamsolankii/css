import matplotlib.pyplot as plt
from collections import Counter
import string

def plot_frequencies(plain_text, cipher_texts, cipher_labels):
    def calculate_normalized_frequencies(text):
        text = text.lower()
        text = ''.join(filter(lambda char: char in string.ascii_lowercase, text))
        freq = Counter(text)
        max_freq = max(freq.values(), default=1)
        normalized_freq = {char: (count / max_freq) * 100 for char, count in freq.items()}
        return normalized_freq

    plain_freq = calculate_normalized_frequencies(plain_text)

    sorted_letters = sorted(plain_freq.items(), key=lambda item: item[1], reverse=True)
    x_labels = [char for char, _ in sorted_letters]

    def prepare_data(freq):
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        sorted_chars = [char for char, _ in sorted_freq]
        sorted_counts = [count for _, count in sorted_freq]
        return sorted_chars, sorted_counts

    plain_chars, plain_counts = prepare_data(plain_freq)

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.plot(range(len(plain_chars)), plain_counts, label='Plain Text', marker='o', linestyle='-', color='blue')

    for i, cipher_text in enumerate(cipher_texts):
        cipher_freq = calculate_normalized_frequencies(cipher_text)
        cipher_chars, cipher_counts = prepare_data(cipher_freq)
        ax.plot(range(len(cipher_chars)), cipher_counts, label=cipher_labels[i], marker='o', linestyle='-', color=plt.cm.tab10(i))

    ax.set_title('Normalized Character Frequency Comparison by Frequency Rank')
    ax.set_xlabel('Frequency Rank')
    ax.set_ylabel('Frequency (%)')
    ax.legend()
    ax.grid(True)

    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels, rotation=90)

    plt.show()

with open("plain-text.txt", "r") as file:
    plain_text = file.readline().strip()

cipher_texts = []
with open("cipher-text.txt", "r") as file:
    for line in file:
        cipher_texts.append(line.strip())

cipher_labels = [
    "Caesar Cipher",
    "Monoalphabetic Cipher",
    "PlayFair Cipher",
    "Hill Cipher",
    "Polyalphabetic Cipher",
]

plot_frequencies(plain_text, cipher_texts, cipher_labels)