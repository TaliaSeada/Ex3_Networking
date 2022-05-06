from socket import *
import sys 

# the URL
# http://127.0.0.1:13000/HelloWorld.html

serverSocket = socket(AF_INET, SOCK_STREAM)
#preparing socket with local host
SERVER_ADDRESS = ('', 13000)
serverSocket.bind(SERVER_ADDRESS)
# waiting for 1 connection
serverSocket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    # accepting the connection
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        # reading the file name to read
        filename = message.split()[1]
        f = open(filename[1:])
        # reading the file
        outputdata = f.read()

        # Send one HTTP header line into socket
        # sending the ok messege for the request
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")

        # Send the content of the requested HTML file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # printing not found to know there is a problem
        print("404 Not Found")
        # sending a fault messege incase of 404
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        f = open("NotFound.html")
        outputdata = f.read()
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        # Closing the connection client socket
        connectionSocket.close()
        break

# closing the entire server
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
