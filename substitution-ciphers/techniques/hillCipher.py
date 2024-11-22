import numpy as np

class HillCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def mod_inverse(self, matrix, modulus):
        det = int(round(np.linalg.det(matrix))) % modulus
        inv_det = pow(det, -1, modulus)
        matrix_mod_inv = inv_det * np.round(np.linalg.det(matrix) * np.linalg.inv(matrix)).astype(int) % modulus
        return matrix_mod_inv

    def hill_cipher_encrypt(self, plaintext, key):
        # Convert key from letters to numbers
        key_matrix = np.array([[self.alphabet.index(key[i * 2 + j]) for j in range(2)] for i in range(2)])
        key_size = key_matrix.shape[0]

        # Convert plaintext to numbers
        plaintext_numbers = [self.alphabet.index(char) for char in plaintext.upper() if char in self.alphabet]

        # Pad plaintext to make sure its length is a multiple of key_size
        padded_plaintext = plaintext_numbers + [0] * ((key_size - len(plaintext_numbers) % key_size) % key_size)

        ciphertext = ""
        for i in range(0, len(padded_plaintext), key_size):
            block = np.array(padded_plaintext[i:i + key_size])
            encrypted_block = np.dot(key_matrix, block) % 26
            ciphertext += ''.join(self.alphabet[int(num)] for num in encrypted_block)
        return ciphertext

    def hill_cipher_decrypt(self, ciphertext, key):
        # Convert key from letters to numbers
        key_matrix = np.array([[self.alphabet.index(key[i * 2 + j]) for j in range(2)] for i in range(2)])
        inverse_key_matrix = self.mod_inverse(key_matrix, 26)

        # Convert ciphertext to numbers
        ciphertext_numbers = [self.alphabet.index(char) for char in ciphertext.upper() if char in self.alphabet]

        plaintext_numbers = []
        for i in range(0, len(ciphertext_numbers), key_matrix.shape[0]):
            block = np.array(ciphertext_numbers[i:i + key_matrix.shape[0]])
            decrypted_block = np.dot(inverse_key_matrix, block) % 26
            plaintext_numbers.extend(int(num) for num in decrypted_block)

        # Remove padding (trailing zeros)
        while plaintext_numbers and plaintext_numbers[-1] == 0:
            plaintext_numbers.pop()

        plaintext = ''.join(self.alphabet[num] for num in plaintext_numbers)
        return plaintext

cipher = HillCipher()

choice = int(input("What do you want to do?\n1. Encrypt\n2. Decrypt\nYour choice: "))

if choice == 1:
    with open("plain-text.txt", "r") as inputFile:
        key = inputFile.readline().strip()
        text = inputFile.readline().strip()
    
    result = key + "\n" + cipher.hill_cipher_encrypt(text, key)
    
    with open("cipher-text.txt", "w") as outputFile:
        outputFile.write(result)

    print("Encryption completed successfully.")
elif choice == 2:
    with open("cipher-text.txt", "r") as inputFile:
        key = inputFile.readline().strip()
        text = inputFile.readline().strip()
    
    result = key + "\n" + cipher.hill_cipher_decrypt(text, key)

    with open("outplain-text.txt", "w") as outputFile:
        outputFile.write(result)

    print("Decryption completed successfully.")
else:
    print("Invalid choice!")
