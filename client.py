# import socket
from socket import *

# for command line input
import sys
def getData(socket):
	while True:
	# getting the file content
			answer = clientSocket.recv(1024)
			f.write(answer.decode())
			try:
				clientSocket.sendall(b"ping")
			except Exception as e:
				print("socket broke")
				return
flag = True
while flag:
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
		getData(socket)
		print("need to get out")
		flag = False
		break
	except IOError as e:
		error = str(e)
		split1 = error.split()[1]
		split2 = split1.split(']')[0]
		if int(split2) != 104:
			print("error!!! " + str(e))
			break

print("finished getting file")
clientSocket.close()

