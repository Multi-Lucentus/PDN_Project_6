from socket import *

# Create a UDP Socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the client
clientSocket.bind(('127.0.0.1', 10000))

# Input a series of numbers
numbers = input("Enter a list of numbers: ")

# Send the message to the server to multiply
messageBytes = numbers.encode("utf-8")

serverIP = '127.0.0.1'
serverPort = 1234
serverAddress = (serverIP, serverPort)

clientSocket.sendto(messageBytes, serverAddress)

# Receive the message string and output
recvBytes, serverAddress = clientSocket.recvfrom(2048)
recv = recvBytes.decode("utf-8")

# Output the number 
print(f'{recv}')

clientSocket.close()