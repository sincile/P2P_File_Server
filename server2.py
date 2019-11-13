import threading
import socket
import sys

host = '127.0.0.1'
# ports = [a for a in range(1024,65536)]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, 8001))
server.listen(5)

def main():
    while True:
        connection, addr = server.accept()
        clientMessage  = b''
        
        #while True:
        data = connection.recv(1024)
			#if (not data):
                #clientMessage += str(data.decode('utf-8'))
				#break
        print (data.decode('utf-8'))
        
        hello = "Hello from the server"
        hello = hello.encode('utf-8')
        
        connection.sendall(hello)
		
        
        connection.close()
        print('Client disconnected\n')


if __name__ == '__main__':
    main()