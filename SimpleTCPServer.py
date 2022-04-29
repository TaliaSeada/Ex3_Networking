#import socket
from socket import *
import sys
# '' or gethostname()
SERVER_ADDRESS = ('', 55555)
# serverSocket = socket.socket()
serverSocket = socket(AF_INET, SOCK_STREAM)

try:
    serverSocket.bind(SERVER_ADDRESS)
except error as e:
    print('Bind failed. Error Code : ' + str(e[0]) + ' Message ' + e[1])
    sys.exit()    
print('Socket bind complete')

serverSocket.listen(1)
print("The server is waiting for a connection.")

while True:
    connectionSocket, addrClient = serverSocket.accept()
    print("Connection has been established from ",addrClient[0],":",str(addrClient[1]))
    connectionSocket.send(str.encode('Welcome. Please enter your message.\n'))
    count = 0
    while count <=3:
        sentence = connectionSocket.recv(255)
        count +=1
        replySentence = '\nServer output:' + sentence.decode('utf-8') + '\n'
        if not sentence:
            break
        connectionSocket.sendall(str.encode(replySentence))
    connectionSocket.close()
    break
serverSocket.close()
sys.exit(0)
