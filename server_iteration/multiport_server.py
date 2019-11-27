#Author: Christian Clark
#Sub-Authors: Dylan Herbst, Brandon Kresge
#Major: Computer Science - SD
#Creation Date: November 18, 2019
#Due Date: November 30, 2019
#Course: CSC 328 - 010
#Professor Name: Dr. Frye
#Assignment: Download station
#Filename: multiport_server.py
#Purpose: Provide a concurent, multiported file server for the client download station
#NOTE: By default the server binds port 8000 - 8100, it will ignore any ports that are already bound
#NOTE: It's assumed that you are running the server on the KU Unix box as the default path for each user will be
#      /export/home/public
#      If you are not on the linux box, please change the default_path variable to a path to a public folder
#      on the server. Otherwise you are not getting the full experience

#Command to run: python3 multiport_server.py

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
    """
    Description:
        Prints/sends a hello to the client
    Parameters:
        connect - the socket you wish to send the hello to
        message - (optional) a string to send to the client
                  (default) Hello from the server
    Return:
        (No return value)
        Message is sent to the client
    Dependencies:
        Library.py - The download server library file
    """
    Library.write(str(message), connect)


def pwd(connect,path=default_path):
    """
    Description:
        Prints/Sends the user's current directory
    Parameters:
        connect - the socket you wish to send the dir to
        path - (optional) The user's current path held in the client thread as currentDir
               (default) the value of default_path variable
               (example) /Users/Christian
    Return:
        (No return value)
        Path is sent to the client if successful
        Error is sent to the client otherwise
    Dependencies:
        Library.py - The download server library file
    """
    try:
        Library.write(path, connect)
        print("Sent:", path)
    except Exception:
        Library.write("Error getting current path", connect)


def dir(connect,path=default_path):
    """
    Description:
        Prints/sends content in the user's current working directory
    Parameters:
        connect - the socket you wish to send the contents to
        path - (optional) The user's current path held in the client thread as currentDir
               (default) the value of default_path variable
               (example) /Users/Christian
    Return:
        (No return value)
        Path content is sent to the client if successful
        Error is sent to the client otherwise
    Dependencies:
        Library.py - The download server library file
        os - Python's operating system call library
    """
    try:
        path_content = os.listdir(str(path))
        Library.write(path_content, connect)
        print("Sent:", path_content)
    except Exception:
        Library.write("Error getting current path", connect)


def cd(connect,path=default_path):
    """
    Description:
        Changes the user's current working directory on the server
        NOTE: This temporarily moves the server to that working directory as well, but returns to
        the default_path location after completion
    Parameters:
        connect - the socket you wish to send the contents to
        path - (optional) The user's current path held in the client thread as currentDir
               (default) the value of default_path variable
               (example) /Users/Christian
    Return:
        0 (zero) - if the server was able to switch the user to that directory
        -1 (negative one) if the directory cannot be changed, there's a permissions error or unknown error

        The above return values are sent to the client as well
    Dependencies:
        Library.py - The download server library file
        os - Python's operating system call library
    """
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
    """
    Description:
        Checks to see if a provided file exists on the server
    Parameters:
        path - (optional) The user's current path held in the client thread as currentDir
               (default) the value of default_path variable
               (example) /Users/Christian
        file - (string) file name and extension
               (example) server.py
    Return:
        True - if the file exists on the server
        False - if the file DNE
    Dependencies:
        Library.py - The download server library file
        os - Python's operating system call library
    """
    return os.path.isfile(path+'/'+str(file))


def download(connect,path=default_path,file='*'):
    """
    Description:
        Download the requested file
        NOTE: There are preconditions (sends READY twice) the client must meet before this function activates
        NOTE: The library write function handles EOF conditions
    Parameters:
        connect - the socket you wish to send the contents to
        path - (optional) The user's current path held in the client thread as currentDir
               (default) the value of default_path variable
               (example) /Users/Christian
        file - (string) file name and extension
               (example) server.py
    Return:
        (No return value)
        File content is sent to the client if successful
        Error is sent to the client otherwise
    Dependencies:
        os - Python's operating system call library

    """
    try:
        with open(path+'/'+file, 'r') as file_content:
            content = file_content.read()
        Library.write(content, connect)
        print("Sent: ", content)
    except (Exception, FileNotFoundError, PermissionError) as e:
        print('Unable to proccess file')
        Library.write('Unable to proccess file', connect)


def create_socket(portNumber):
    """
    Description:
        Creates a passive socket on the given port
        NOTE: each socket has a max listening queue value of 10
    Parameters:
        portNumber (int) - the port number you wish to make the
    Return:
        server (socket) - a (passive) listening socket on the requested port number
    Dependencies:
        socket - Python's socket library
    """
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
    """
    Description:
        This is the default client loop that proccesses the client's request when the server accepts connection
        NOTE: The server always sends a hello because it's a nice person
        NOTE: It's assumed that the connection is called inside a thread
        NOTE: Every client connecting always starts off in the same path (default_path)
        NOTE: Each client has their own path specified by the currentDir variable
    Commands/Messages proccessed:
        PWD
        DIR
        CD
        DOWNLOAD
        BYE
    Parameters:
        connect - the socket you wish to send the contents to
    Return:
        (No return value)
        Loop ends and connection closes under the following conditions:
            1. The client sends the BYE message
            2. The client sends empty input
            3. There's a socket error such as when the client disconnects without saying goodbye
            4. There's a pipe error during the connection
    Dependencies:
        Library.py - The download server library file
        socket - Python's socket library
    """
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

    #Listen on all ports in the given range
    #Default listening ports: 8000 - 8100
    for port in range(8000,8101):
          try:
              connection_list.append(create_socket(port))
          except Exception:
              print("Cannot bind port: ", port)
              error_list.append(port)
              pass

    #report any issues making the ports listen
    if error_list:
        print("NOTE that these ports are not bound due to an unknown error: ", error_list)

    #start the loop and wait for any connection
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
