from socket import *

# Create a TCP Socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort)

clientSocket.connect(serverAddress)

# Get the number list from the user to send to the server for multiplication
numbers = input("Input a list of numbers: ")

clientSocket.send(numbers.encode("utf-8"))

# Get the message back from the server
recv = clientSocket.recv(1024)
print(recv.decode("utf-8"))

clientSocket.close()