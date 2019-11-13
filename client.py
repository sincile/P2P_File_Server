import sys
import socket

def connect(portNumber):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket
    except:
        print 'Error creating socket'
        sys.exit(-1)
		
    server_address = ('127.0.0.1', portNumber)
    
    try:
        sock.connect(server_address) #Create connection to server
    except:
        print 'Error creating connection'
        sys.exit(-1)
		
        
    msg = 'Hello from the client'   
    msg = msg.encode('utf-8')    
        
    try:
		sock.sendall(msg) #Send message to server
    except:
		print 'Error sending hello'
		sys.exit(-1)
		
    try:    
        msg = sock.recv(512) #Receive message from server
    except:
        print 'Receive error'
        sys.exit(-1)
        
    try:    
        close = sock.close() #Close socket
    except:
        print 'Error closing socket'
        sys.exit(-1)
    print msg
    return

def main (hostName, portNumber):
    print hostName
    print portNumber
    
    connect(portNumber)

    return

if (len(sys.argv) < 2 or len(sys.argv) > 3): #Make sure format of command line arguments is correct
    print 'Usage: ', sys.argv[0], '<hostName> <portNumber (Optional)> \n' #Print usage clause if command line arguments are input incorrectly
    sys.exit()
    
if (len(sys.argv) == 2):
    portNumber = 8001
    
else:
    portNumber = sys.argv[2]
    
main(sys.argv[1], portNumber)
