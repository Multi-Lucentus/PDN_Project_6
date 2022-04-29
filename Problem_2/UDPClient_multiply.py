from socket import *

# Create a UDP Socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Input a series of numbers
message = ''
input = ''
while input != 'quit':
    # Ask the user for a new number
    input = input()

    # Append the number to the end
    if(input != 'quit'):
        message = message + ',' + input

# Send the message to the server to multiply
messageBytes = message.encode("utf-8")

serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort)

clientSocket.sendto(messageBytes, serverAddress)

# Receive the message string and output
recvBytes, serverAddress = clientSocket.recvfrom(2048)
recv = recvBytes.decode("utf-8")

clientSocket.close()

# Output the number 
print(recv)