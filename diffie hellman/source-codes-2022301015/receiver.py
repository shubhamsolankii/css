import socket
import diffie_hellman
import polyalphabetic

sharedSecretKey = None

def displayMenu():
    print("Waiting for connections...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind(("localhost", 3333))
        serverSocket.listen()

        while True:
            connection, address = serverSocket.accept()
            with connection:
                print(f"Connected by {address}")
                if handleClientConnection(connection):
                    print("Exit signal received. Shutting down the receiver.")
                    break 

def handleClientConnection(connection):
    global sharedSecretKey
    receivedMessage = connection.recv(1024).decode()

    if receivedMessage == "exit":
        return True

    if sharedSecretKey is None:
        senderPartialKey = int(receivedMessage)
        print(f"Sender Partial Key (A): {senderPartialKey}")

        primeNumber = int(input("Enter prime number (P): "))
        primitiveRoot = int(input("Enter primitive root (G): "))
        privateKeyB = int(input("Enter private key (b): "))

        receiverPartialKey = diffie_hellman.generatePartialKey(primeNumber, primitiveRoot, privateKeyB)
        print(f"Receiver Partial Key (B): {receiverPartialKey}")
        connection.sendall(str(receiverPartialKey).encode())

        sharedSecretKey = diffie_hellman.generateSharedKey(senderPartialKey, privateKeyB, primeNumber)
        print(f"Shared Secret Key: {sharedSecretKey}")
    else:
        encryptedMessage = receivedMessage
        decryptedMessage = polyalphabetic.decryptMessage(encryptedMessage, str(sharedSecretKey))
        print(f"Decrypted message: {decryptedMessage}")
    
    return False

if __name__ == "__main__":
    displayMenu()
