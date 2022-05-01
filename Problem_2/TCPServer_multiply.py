from socket import *

# Create a TCP Socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind to local IP and port 12345
serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort)
serverSocket.bind(serverAddress)

# Begin listening for TCP requests
serverSocket.listen(1)
while True:
    # Get information from client
    connectionSocket, clientAddress = serverSocket.accept()
    clientIP, clientPort = clientAddress

    print("Connected to client at " + clientIP)

    # Receive the message in bytes from the client
    msgBytes = connectionSocket.recv(1024)
    message = msgBytes.decode("utf-8")

    # Parse the message, and multiply the numbers
    numbers = message.split(",")

    try:
        product = 1
        for num in numbers:
            product = product * float(num)

        msg = str(product)

        # Send the product back to the client
        connectionSocket.send(msg.encode("utf-8"))
    except:
        # Print "Invalid Message to the client"
        invalid = "Invalid Message"
        connectionSocket.send(invalid.encode("utf-8"))
    
    connectionSocket.close()