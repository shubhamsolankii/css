import asyncio
import websockets
import rsa
import polyalphabetic

rsaPrivateKey = None
sharedEncryptionKey = None


async def startMessageSender():
    while True:
        print("\n1) To register public key - register <name> <key>")
        print("2) To get public key - get <name>")
        print("3) To send message - connect <name> <ip:port>")
        print("4) To exit - exit\n")
        userCommand = input("Enter command: ")
        print()

        await executeCommand(userCommand)


async def executeCommand(userCommand):
    commandName = userCommand.split(' ')[0]
    if commandName == "register":
        await registerPublicKey(userCommand)
    elif commandName == "get":
        await getPublicKey(userCommand)
    elif commandName == "connect":
        await connectToServer(userCommand)
    else:
        print("Unknown command")


async def registerPublicKey(userCommand):
    global rsaPrivateKey
    commandParts = userCommand.split(' ')
    primeNumbers = commandParts[2]
    primeP, primeQ = primeNumbers.split(',')
    primeP, primeQ = int(primeP), int(primeQ)
    modulusN, publicExponent, privateExponent = rsa.generateRsaKeyPair(primeP, primeQ)
    publicKey = f"{modulusN},{publicExponent}"
    rsaPrivateKey = f"{modulusN},{privateExponent}"

    print(f"Public key generated for {commandParts[1]}")
    print(f"Modulus: {modulusN}, Public Exponent: {publicExponent}")
    print()

    async with websockets.connect('ws://localhost:3000') as websocketConnection:
        await websocketConnection.send(f"{commandParts[0]} {commandParts[1]} {publicKey}")
        serverResponse = await websocketConnection.recv()
        print(serverResponse)


async def getPublicKey(userCommand):
    async with websockets.connect('ws://localhost:3000') as websocketConnection:
        await websocketConnection.send(userCommand)
        publicKeyResponse = await websocketConnection.recv()
        print(publicKeyResponse)
        return publicKeyResponse


async def connectToServer(userCommand):
    _, name, address = userCommand.split(' ')
    ipAddress, portNumber = address.split(':')
    publicKey = None
    try:
        publicKey = await getPublicKey("get " + name)
    except:
        print("Public key not found")
        return

    modulusN, publicExponent = publicKey.split(',')
    modulusN, publicExponent = int(modulusN), int(publicExponent)
    print(f"Public key received for {name}")
    print(f"Modulus: {modulusN}, Public Exponent: {publicExponent}")
    print()

    sharedKey = input("Enter shared key: ")
    print()

    global sharedEncryptionKey
    sharedEncryptionKey = sharedKey

    async with websockets.connect(f"ws://{ipAddress}:{portNumber}") as websocketConnection:
        await websocketConnection.send(f"{rsa.rsaEncryptMessage(sharedKey, modulusN, publicExponent)}")
        serverResponse = await websocketConnection.recv()
        print(serverResponse)

        if serverResponse == "OK":
            while True:
                userMessage = input("Enter message: ")
                if userMessage == "exit":
                    break
                cipherText = polyalphabetic.encryptMessage(userMessage, sharedKey)
                await websocketConnection.send(cipherText)
                serverResponse = await websocketConnection.recv()
                print(serverResponse)

asyncio.run(startMessageSender())