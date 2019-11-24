from _thread import *
import socket
import sys
import os
import Library

host = '127.0.0.1'

def create_socket(portNumber):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    print("Socket made")
    try:
        server.bind((host, portNumber))
    except socket.error:
        print("Error when binding")
        sys.exit()

    print("Socket bound")
    server.listen(1)
    print("Socket is listening on: ", portNumber)
    return server


def client_connection(connect):
    connect.send(("Hello from the server\n").encode('utf-8'))
    while True:
        data = connect.recv(1024)
        server_reply = "Client data: " + data.decode('utf-8')
        if not data:
            break
        print(server_reply.encode('utf-8'))
        connect.sendall(("Recieved: " + server_reply).encode('utf-8'))
    connect.close()


def main():
    # connection_list = []
    server_sock = create_socket(8005)
    # connection_list.append(server_sock)

    while True:
        connect, addr = server_sock.accept()
        print("Connected with " + addr[0] + ":" + str(addr[1]))
        start_new_thread(client_connection, (connect,))

    server_sock.close()

if __name__ == '__main__':
    main()
