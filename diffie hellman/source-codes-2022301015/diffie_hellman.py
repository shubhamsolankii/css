def generatePartialKey(primeNumber, generator, privateKey):
    return pow(generator, privateKey, primeNumber)

def generateSharedKey(partialKey, privateKey, primeNumber):
    return pow(partialKey, privateKey, primeNumber)
