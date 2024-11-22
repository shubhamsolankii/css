import asyncio
import websockets
import rsa
import polyalphabetic

rsaPrivateKey = None
sharedEncryptionKey = None


async def startMessageSender():
    while True:
        print("\n1) To register public key - register <name> <key>")
        print("2) Wait for messages - receive")
        print("3) To exit - exit\n")
        commandInput = input("Enter command: ")
        print()

        await sendCommand(commandInput)


async def sendCommand(commandInput):
    commandName = commandInput.split(' ')[0]
    if commandName == "register":
        await registerPublicKey(commandInput)
    elif commandName == "receive":
        await receiveMessages(commandInput)
    else:
        print("Unknown command")


async def registerPublicKey(commandInput):
    global rsaPrivateKey
    commandParts = commandInput.split(' ')
    primeNumbers = commandParts[2]
    p, q = primeNumbers.split(',')
    p, q = int(p), int(q)
    modulus, publicExponent, privateExponent = rsa.generateRsaKeyPair(p, q)
    publicKey = f"{modulus},{publicExponent}"
    rsaPrivateKey = f"{modulus},{privateExponent}"

    print(f"Public key generated for {commandParts[1]}")
    print(f"Modulus: {modulus}, Public Exponent: {publicExponent}")
    print()

    async with websockets.connect('ws://localhost:3000') as websocketConnection:
        await websocketConnection.send(f"{commandParts[0]} {commandParts[1]} {publicKey}")
        serverResponse = await websocketConnection.recv()
        print(serverResponse)


async def receiveSharedKeyAndMessages(websocketConnection):
    global sharedEncryptionKey
    receivedSharedKey = False
    while not receivedSharedKey:
        encryptedKey = await websocketConnection.recv()
        decryptedKey = rsa.rsaDecryptMessage(encryptedKey, int(rsaPrivateKey.split(',')[0]), int(rsaPrivateKey.split(',')[1]))
        sharedEncryptionKey = decryptedKey
        receivedSharedKey = True
        await websocketConnection.send("OK")

    print(f"Shared key received: {sharedEncryptionKey}")
    
    while True:
        encryptedMessage = await websocketConnection.recv()
        decryptedMessage = polyalphabetic.decryptMessage(encryptedMessage, sharedEncryptionKey)
        print(f"Received message: {decryptedMessage}")
        await websocketConnection.send("OK")


async def receiveMessages(commandInput):
    server = await websockets.serve(receiveSharedKeyAndMessages, "localhost", 4000)
    print("Receive server started on ws://localhost:4000")
    await server.wait_closed()


asyncio.run(startMessageSender())