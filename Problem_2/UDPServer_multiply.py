from http import server
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the local IP and port 12345
serverIP = '127.0.0.1'
serverPort = 1234
serverAddress = (serverIP, serverPort)
serverSocket.bind(serverAddress)

print('Server is ready for clients')

while True: 
    # Receive a list of numbers from the client and multiply them
    # List format is: number1,number2,number3,...
    messageBytes, clientAddress = serverSocket.recvfrom(2048)
    clientIP, clientPort = clientAddress

    print("Connected to client at " + clientIP)

    # Decode the message bytes
    message = messageBytes.decode("utf-8")

    # Split the message by commas
    numbers = message.split(",")

    # Multiply all the numbers together and send back to the user
    # Surround w/ a try-catch block to catch input errors
    try:
        product = 1
        for num in numbers:
            product = product * float(num)
        msg = str(product)
        serverSocket.sendto(msg.encode("utf-8"), clientAddress)
    except:
        # Print "Invalid Message to the client"
        invalid = "Invalid Message"
        serverSocket.sendto(invalid.encode("utf-8"), clientAddress)

