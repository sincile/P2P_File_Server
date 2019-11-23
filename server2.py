import threading
import socket
import sys
import Library
import os

host = '127.0.0.1'
# ports = [a for a in range(1024,65536)]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, 8118))
server.listen(5)


def PWD():
    try:
        currentDir = os.getcwd()
    except:
        error = 'getcwd error'
        return error
    return currentDir
        
    
def DIR():
    try:
        directoryListing = os.listdir()
    except:
        error = 'listdir error'
        return error
        
    return directoryListing
    
def CD(connection):
    newDirectory = Library.read(connection)
    
    try:
        os.chdir(newDirectory)
    except:
        print ('chdir error')
        
    return

def main():

    connection, addr = server.accept()
    data = Library.read(connection)
    print (data)
    hello = "Hello from the server"
    Library.write(hello, connection)
    
    while True:
    
        clientMessage  = ''
        data = Library.read(connection)
        
        if data == 'PWD':
            currentDir = PWD()
            Library.write(currentDir, connection)
        elif data == 'DIR':
            directoryListing = DIR()
            Library.write(directoryListing, connection)
        elif data == 'CD':
            CD(connection)
        elif (data == 'BYE'):
            print (data)
            break
        
		
        
    connection.close()
    print('Client disconnected\n')


if __name__ == '__main__':
    main()
