import threading
import socket
import sys

host = '127.0.0.1'
# ports = [a for a in range(1024,65536)]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((host,8080))
server.listen()
print("Listening on ", host, ' on port 8080' )

def main():
    while True:
        connection, addr = server.accept()
        clientMessage  = ''

        while True:
            data = connection.recv(1024)
            if (not data):
                clientMessage +=data
            print (clientMessage)

            connection.send(b'Hello from the server\n')

        connection.close()
        print(b'Client disconnected\n')


if __name__ == '__main__':
    main()
