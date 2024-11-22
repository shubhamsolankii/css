import socket
import diffie_hellman
import sympy
import polyalphabetic

sharedSecretKey = None

def displayMenu():
    while True:
        print("\n1) Generate key using Diffie-Hellman")
        print("2) Send message to receiver")
        print("3) Exit\n")
        userOption = input("Enter option: ")
        print()

        if userOption == "1":
            generateSharedKey()
        elif userOption == "2":
            sendMessageToReceiver()
        elif userOption == "3":
            exitProgram()
            print("Exiting...")
            break
        else:
            print("Invalid option.")

def generateSharedKey():
    global sharedSecretKey
    primeNumber = int(input("Enter prime number (P): "))
    primitiveRoot = int(input("Enter primitive root (G): "))
    privateKeyA = int(input("Enter private key (a): "))
    
    senderPartialKey = diffie_hellman.generatePartialKey(primeNumber, primitiveRoot, privateKeyA)
    print(f"Sender Partial Key (A): {senderPartialKey}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as senderSocket:
        senderSocket.connect(("localhost", 3333))
        senderSocket.sendall(str(senderPartialKey).encode())
        receiverPartialKey = int(senderSocket.recv(1024).decode())

    sharedSecretKey = diffie_hellman.generateSharedKey(receiverPartialKey, privateKeyA, primeNumber)
    print(f"Shared Secret Key: {sharedSecretKey}")

def sendMessageToReceiver():
    global sharedSecretKey
    if sharedSecretKey is None:
        print("Generate the key first!")
        return

    messageToSend = input("Enter a message: ")

    encryptedMessage = polyalphabetic.encryptMessage(messageToSend, str(sharedSecretKey))
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as senderSocket:
        senderSocket.connect(("localhost", 3333))
        senderSocket.sendall(encryptedMessage.encode())
        print("Message sent to receiver.")

def exitProgram():
    """Notify the receiver that the sender is exiting."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as senderSocket:
        senderSocket.connect(("localhost", 3333))
        senderSocket.sendall("exit".encode()) 
        print("Exit signal sent to receiver.")

if __name__ == "__main__": 
    displayMenu()
