import itertools

def generate_key_matrix(key):
    key = "".join(sorted(set(key), key=key.index))
    key += "".join([chr(i) for i in range(65, 91) if chr(i) not in key and chr(i) != 'J'])
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def get_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def decrypt_digram(digram, matrix):
    r1, c1 = get_position(digram[0], matrix)
    r2, c2 = get_position(digram[1], matrix)
    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_playfair(ciphertext, key):
    matrix = generate_key_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_digram(ciphertext[i:i+2], matrix)
    return plaintext

ciphertext = "BMODZBXDNABEKUDMUIXMMOUVIF"
keys = ["CIPHER", "CRYPTO", "RANDOM", "PASSWORD"]

results = []
for key in keys:
    decrypted_text = decrypt_playfair(ciphertext, key)
    results.append(f"Key: {key} -> Decrypted Text: {decrypted_text}")

with open("attack-results.txt", "w") as file:
    file.write("\n".join(results))
