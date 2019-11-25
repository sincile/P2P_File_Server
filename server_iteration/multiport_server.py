from _thread import *
import socket
import select
import sys
import os
import Library

host = '127.0.0.1'
terminating_char = "*?*"

def hello(connect, message="Hello from the server"):
    Library.write(message, connect)

def pwd(connect):
    try:
        path = os.getcwd()
        Library.write(path, connect)
        print("Sent:", path)
    except Exception:
        Library.write("Error getting current path", connect)

def dir(connect,path=''):
    try:
        if(path):
            path_content = os.listdir(path)
        else:
            path_content = os.listdir()
        Library.write(path_content, connect)
        print("Sent:", path_content)
    except Exception:
        Library.write("Error getting current path", connect)

def cd(connect,path=''):
    try:
        if(path):
            path_content = os.chdir(path)
        else:
            path_content = os.chdir('/')
        Library.write(path_content, connect)
        print("Sent:", path_content)
        return path_content
    except Exception:
        Library.write("Error getting current path", connect)

def download(connect,path='/',file='*'):
    Library.write("This don't work yet chief", connect)
    print("Sent: " + "nothing lmao")

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
    server.listen(10)
    print("Socket is listening on: ", portNumber)
    return server


def client_connection(connect):
    hello(connect)
    currentDir = '/'
    while True:
        try:
            data = Library.read(connect)
            server_reply = "Got: " + data
            if data == 'PWD':
                pwd(connect)
            if data == 'DIR':
                dir(connect)
            if data == 'CD':
                data = Library.read(connect)
                currentDir = cd(connect,data)
            if data == 'DOWNLOAD':
                download(connect)
            if data == 'BYE':
                connect.close()
                break
            if not data:
                connect.close()
                break
            print(server_reply)
            # connect.send(("Server Recieved: " + server_reply + terminating_char).encode('utf-8'))
        except socket.error:
            print("Client disconnected")
            connect.close()
        except IOError:
            print("PIPE error")
            connect.close()


def main():
    connection_list = []
    for port in range(8000,8101):
          try:
              connection_list.append(create_socket(port))
          except Exception:
              pass

    while True:
        #Monitor all conenction ports for activity
        s_read, s_write, s_error = select.select(connection_list,[],[])

        #Accept all clients wanting to connect
        for sock in s_read:
            connect, addr = sock.accept()
            try:
                #auto handle threads using the client connection
                start_new_thread(client_connection, (connect,))
            except Exception:
                print("Can't create client thread")
                pass

    #Close all the sockets
    for i in connection_list:
        try:
            connection_list[i].close()
        except Exception:
            pass


if __name__ == '__main__':
    main()
