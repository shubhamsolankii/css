def greatestCommonDivisor(numberA, numberB):
    if numberA == 0:
        return numberB, 0, 1
    gcdValue, coefficientX, coefficientY = greatestCommonDivisor(numberB % numberA, numberA)
    return gcdValue, coefficientY - (numberB // numberA) * coefficientX, coefficientX


def modularInverse(numberA, modulusM):
    gcdValue, coefficientX, coefficientY = greatestCommonDivisor(numberA, modulusM)
    if gcdValue != 1:
        raise Exception("Inverse Modulo doesn't exist")
    return coefficientX % modulusM


def modularExponentiation(base, exponent, modulusM):
    result = 1
    for _ in range(exponent):
        result *= base % modulusM
    return result % modulusM


def isPrime(numberN):
    if numberN < 2:
        return False

    for divisor in range(2, numberN):
        if numberN % divisor == 0:
            return False

    return True


def selectPublicExponent(primeP, primeQ):
    limit = (primeP - 1) * (primeQ - 1)
    publicExponent = 2
    while publicExponent < limit:
        try:
            modularInverse(publicExponent, limit)
            break
        except:
            publicExponent += 1
    return publicExponent


def encryptMessage(message, modulusN, publicExponent):
    return modularExponentiation(message, publicExponent, modulusN)


def decryptMessage(ciphertext, modulusN, privateExponent):
    return modularExponentiation(ciphertext, privateExponent, modulusN)


def rsaEncryptMessage(message, modulusN, publicExponent):
    return ''.join([chr(encryptMessage(ord(char), modulusN, publicExponent)) for char in message])


def rsaDecryptMessage(ciphertext, modulusN, privateExponent):
    return ''.join([chr(decryptMessage(ord(char), modulusN, privateExponent)) for char in ciphertext])


def generateRsaKeyPair(primeP, primeQ):
    publicExponent = selectPublicExponent(primeP, primeQ)
    totient = (primeP - 1) * (primeQ - 1)
    privateExponent = modularInverse(publicExponent, totient)
    modulusN = primeP * primeQ
    return modulusN, publicExponent, privateExponent


