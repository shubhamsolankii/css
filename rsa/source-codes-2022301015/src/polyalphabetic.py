def encryptMessage(message, encryptionKey):
    encryptionKey = encryptionKey.upper()
    encryptionKeyLength = len(encryptionKey)
    encryptionKeyInt = [ord(char) - 65 for char in encryptionKey]
    messageLength = len(message)
    messageInt = [ord(char) - 65 for char in message]
    cipherText = ""
    
    for index in range(messageLength):
        cipherText += chr(((messageInt[index] + encryptionKeyInt[index % encryptionKeyLength])) + 65)
    
    return cipherText


def decryptMessage(cipherText, decryptionKey):
    decryptionKey = decryptionKey.upper()
    decryptionKeyLength = len(decryptionKey)
    decryptionKeyInt = [ord(char) - 65 for char in decryptionKey]
    cipherTextLength = len(cipherText)
    cipherTextInt = [ord(char) - 65 for char in cipherText]
    message = ""
    
    for index in range(cipherTextLength):
        message += chr(((cipherTextInt[index] - decryptionKeyInt[index % decryptionKeyLength])) + 65)
    
    return message
