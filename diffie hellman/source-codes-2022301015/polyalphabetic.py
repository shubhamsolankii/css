def encryptMessage(message, encryptionKey):
    encryptionKey = encryptionKey.upper()
    encryptionKeyLength = len(encryptionKey)
    encryptionKeyIntegers = [ord(char) - 65 for char in encryptionKey]
    messageLength = len(message)
    messageIntegers = [ord(char) - 65 for char in message]
    cipherText = ""
    for index in range(messageLength):
        cipherText += chr(((messageIntegers[index] + encryptionKeyIntegers[index % encryptionKeyLength])) + 65)
    return cipherText


def decryptMessage(cipherText, decryptionKey):
    decryptionKey = decryptionKey.upper()
    decryptionKeyLength = len(decryptionKey)
    decryptionKeyIntegers = [ord(char) - 65 for char in decryptionKey]
    cipherTextLength = len(cipherText)
    cipherTextIntegers = [ord(char) - 65 for char in cipherText]
    decryptedMessage = ""
    for index in range(cipherTextLength):
        decryptedMessage += chr(((cipherTextIntegers[index] - decryptionKeyIntegers[index % decryptionKeyLength])) + 65)
    return decryptedMessage
