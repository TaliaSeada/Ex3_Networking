# import socket
from socket import *

# for command line input
import sys

# to check if socket is up
def is_connect(sock):
	try:
		sock.sendall(b"ping")
		return True
	except:
		return False
	
while True:
	try:

		serverName = sys.argv[1] # IP
		serverPort = int(sys.argv[2]) # PORT
		SERVER_ADDRESS = (serverName, serverPort)

		clientSocket = socket(AF_INET, SOCK_STREAM)
		clientSocket.connect(SERVER_ADDRESS)
		file = sys.argv[3] # filename
		request = "GET /" + file 
		clientSocket.send(request.encode())
		answer = clientSocket.recv(1000)
        # ok messege
		print("from server: " + str(answer.decode() + " now on to the file!"))
        # opening file
		f = open(file, "w")
		while True:
			if is_connect(clientSocket) == False:
				break
            # getting the file content
			answer = clientSocket.recv(1024)
			f.write(answer.decode())
		break
	except IOError as e:
		error = str(e)
		split1 = error.split()[1]
		split2 = split1.split(']')[0]
		if int(split2) != 104:
			print("error!!! " + str(e))

print("finished getting file")
clientSocket.close()

