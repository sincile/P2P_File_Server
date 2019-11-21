import sys
import socket
import os

def PWD():
    print('PWD')
    return
    
def DIR():
    print('DIR')
    return
    
def CD():
    print('CD')
    return
    
def LPWD():
    try:
        currentDir = os.getcwd()
    except:
        print('getcwd error')
        return
        
    print ('Current directory: ', currentDir, '\n')
    return
    
def LDIR():
    try:
        directoryListing = os.listdir()
    except:
        print ('listdir error')
        
    print (directoryListing, '\n')
    return
    
def LCD():
    newDirectory = input('Please enter directory you would like to change to: ')
    
    try:
        os.chdir(newDirectory)
    except:
        print('chdir error')
        
    try:
        currentDir = os.getcwd()
    except:
        print('getcwd error')
        return
        
    print('Current directory: ', currentDir, '\n')
    return
    
def Download():
    print('Download')
    return

def menu():
     
    loop = True
     
    while loop:
    
        print ('1 - PWD')
        print ('2 - DIR')
        print ('3 - CD')
        print ('4 - LPWD')
        print ('5 - LDIR')
        print ('6 - LCD')
        print ('7 - Download')
        print ('8 - Exit')
        selection = input('Please enter the corresponding number of the option you would like to select: ')
    
        if int(selection) == 1:
            PWD()
        elif int(selection) == 2:
            DIR()
        elif int(selection) == 3:
            CD()
        elif int(selection) == 4:
            LPWD()
        elif int(selection) == 5:
            LDIR()
        elif int(selection) == 6:
            LCD()
        elif int(selection) == 7:
            Download()
        elif int(selection) == 8:
            loop = False
        else:
            print('Invalid selection.')
        
    return

def connect(IP, portNumber):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket
    except:
        print ('Error creating socket')
        sys.exit(-1)
		
    server_address = (IP, int(portNumber))
    
    
    try:
        sock.connect(server_address) #Create connection to server
    except:
        print ('Error creating connection')
        sys.exit(-1)
        
    msg = ('Hello from the client')   
    msg = msg.encode('utf-8')    
    
    try:
        sock.sendall(msg) #Send message to server
    except:
        print ('Error sending hello')
        sys.exit(-1)
		
    try:    
        msg = sock.recv(512) #Receive message from server
    except:
        print ('Receive error')
        sys.exit(-1)
        
    menu()
        
    try:    
        close = sock.close() #Close socket
    except:
        print ('Error closing socket')
        sys.exit(-1)
        
    msg = msg.decode('utf-8')
    print (msg)
    return

def main (hostName, portNumber):
    print (hostName)
    print (portNumber)
    
    connect(IP, portNumber)

    print('Client program ended.')
    return

if (len(sys.argv) < 2 or len(sys.argv) > 3): #Make sure format of command line arguments is correct
    print ('Usage: ', sys.argv[0], '<hostName> <portNumber (Optional)> \n') #Print usage clause if command line arguments are input incorrectly
    sys.exit()
    
IP = sys.argv[1]
    
if (len(sys.argv) == 2):
    portNumber = 8000
    
else:
    portNumber = sys.argv[2]
    
main(IP, portNumber)
