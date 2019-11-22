import threading
import socket
import sys
import Library

host = '127.0.0.1'
# ports = [a for a in range(1024,65536)]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, 8393))
server.listen(5)

def main():
    while True:
        connection, addr = server.accept()
        clientMessage  = b''
        
        #while True:
        data = Library.read(connection)
			#if (not data):
                #clientMessage += str(data.decode('utf-8'))
				#break
        print (data)
        
        hello = "Hello from the server"
        hello = hello.encode('utf-8')
        
        connection.sendall(hello)
		
        
        connection.close()
        print('Client disconnected\n')
        break


if __name__ == '__main__':
    main()
