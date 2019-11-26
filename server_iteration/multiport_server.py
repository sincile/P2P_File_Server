from _thread import *
import socket
import select
import sys
import os
import Library

host = '127.0.0.1'
terminating_char = "*?*"
# default_path = "/Users/Christian"
default_path = "/export/home/public"

def hello(connect, message="Hello from the server"):
    Library.write(message, connect)

def pwd(connect,path=default_path):
    try:
        Library.write(path, connect)
        print("Sent:", path)
    except Exception:
        Library.write("Error getting current path", connect)

def dir(connect,path=default_path):
    try:
        path_content = os.listdir(str(path))
        Library.write(path_content, connect)
        print("Sent:", path_content)
    except Exception:
        Library.write("Error getting current path", connect)

def cd(connect,path=default_path):
    try:
        path_content = os.chdir(str(path))
        Library.write('0', connect)
        print("Sent: ", '0')
        #reset server location back to origin
        os.chdir(default_path)
        return 0
    except (Exception, FileNotFoundError, PermissionError) as e:
        Library.write('-1', connect)
        print("Sent: ", '-1')
        return -1

def check_file(path,file):
    return os.path.isfile(path+'/'+file)

def download(connect,path=default_path,file='*'):
    with open(path+'/'+file, 'r') as file_content:
        content = file_content.read()
    Library.write(content, connect)
    print("Sent: ", content)

def create_socket(portNumber):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    print("Socket made")
    try:
        server.bind((host, portNumber))
    except socket.error:
        print("Error when binding on port" + portNumber)
        return
    print("Socket bound")
    server.listen(10)
    print("Socket is listening on: ", portNumber)
    return server


def client_connection(connect):
    hello(connect)
    currentDir = default_path
    while True:
        try:
            data = Library.read(connect)
            server_reply = "Got: " + data
            print(server_reply)

            if data == 'PWD':
                pwd(connect,currentDir)
            if data == 'DIR':
                dir(connect,currentDir)
            if data == 'CD':
                path = Library.read(connect)
                print("Got directory: " + path)
                if (cd(connect, path) != -1):
                    currentDir = path
                else:
                    pass
            if data == 'DOWNLOAD':
                file = Library.read(connect)
                print("File: " + file)
                if (check_file(currentDir,file)):
                    Library.write('READY',connect)
                    print('File exists')
                    clientStatus = Library.read(connect)
                    if (clientStatus == "READY"):
                        print('Client confirmed...starting download')
                        download(connect,currentDir,file);
                    else:
                        print('Client Denied')
                        pass
                else:
                    print('File Not Found')
                    Library.write('File Not Found',connect)
                    pass
            if data == 'BYE':
                print("See you later boo")
                connect.close()
                break
            if not data:
                print("It's empty, closing the port")
                connect.close()
                break
        except socket.error:
            print("Client disconnected")
            connect.close()
        except IOError:
            print("PIPE error")
            connect.close()

def main():
    connection_list = []
    error_list = []
    for port in range(8000,8101):
          try:
              connection_list.append(create_socket(port))
          except Exception:
              print("Cannot bind port: ", port)
              error_list.append(port)
              pass

    if error_list:
        print("NOTE that these ports are not bound due to an unknown error: ", error_list)

    while True:
        #Monitor all conenction ports for activity
        s_read, s_write, s_error = select.select(connection_list,[],[])

        #Accept all clients wanting to connect
        for sock in s_read:
            connect, addr = sock.accept()
            try:
                #auto handle threads using the client connection func
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
