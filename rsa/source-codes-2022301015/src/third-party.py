import asyncio
import websockets

publicKeyDictionary = {}


def registerPublicKey(userName, publicKey):
    publicKeyDictionary[userName] = publicKey


def getPublicKey(userName):
    return publicKeyDictionary[userName]


async def handleClientCommand(websocketConnection, path):
    async for clientMessage in websocketConnection:
        messageParts = clientMessage.lower().strip().split(' ')
        clientCommand = messageParts[0]

        if clientCommand == "register":
            registerPublicKey(messageParts[1], messageParts[2])
            serverResponse = "Public key registered for " + messageParts[1]
            print(f"Public key {messageParts[2]} registered for " + messageParts[1])
            print()
        elif clientCommand == "get":
            serverResponse = getPublicKey(messageParts[1])
            print("Public key requested for " + messageParts[1])
            print(publicKeyDictionary)
        else:
            serverResponse = "Unknown command"

        await websocketConnection.send(serverResponse)


async def startWebSocketServer():
    server = await websockets.serve(handleClientCommand, "localhost", 3000)
    print("WebSocket server started on ws://localhost:3000")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(startWebSocketServer())
