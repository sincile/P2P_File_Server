#***************************************************************
#* 
#* Author: Brandon Kresge
#* Creation Date: November 19, 2019
#* Due Date: November 26th, 2019
#* Python Version: 3.7.3
#* Course: CSC328-010
#* Filename: LibraryTest.py
#* Purpose: Make a library that the client and server can call functions from.
#* To run and compile: ?
#**************************************************************

import os
import socket
#import socketUtils
terminatingstring = "*?*"

#**************************************************************
#Function Name: read
#Description: Reads message to socket
#Parameters: None
#Return value: None
#**************************************************************

#def read():    

#make sure in read byte mode

#**************************************************************
#Function Name: write
#Description: Writes message to socket
#Parameters: None
#Return value: None
#**************************************************************

def write(message, sock):    
    message = str(message) + terminatingstring
    
    message = message.encode('utf-8')
    try:
        sock.sendall(message)
    except:
        print ("Sendall error")
    return
#write byte mode

#read function

def read(sock):
    message = ''
    while True:
        try:
            message = message + sock.recv(256).decode('utf-8')
        except:
            print ("recv error")
            break
        if (message [-3:]==terminatingstring):
            break
    return message[:-3]

#**************************************************************
#Function Name: validate
#Description: Validates input. If input is not from the list of commands, returns an error.
#Parameters: input - user input
#Return value: None
#**************************************************************

def validate(input):
    input = input.upper()
    input = input.split(' ', 1)[0]
    print (input)
    if input == "PWD":
        valid = True
    elif input == "DOWNLOAD":
        valid = True
    elif input == "DIR":
        valid = True
    elif input == "CD":
        valid = True
    elif input == "LPWD":
        valid = True
    elif input == "LDIR":
        valid = True
    elif input == "LCD":
        valid = True
    elif input == "READY":
        valid = True
    elif input == "FILE":
        valid = True
    elif input == "STOP":
        valid = True
    else: 
        valid = False
    return valid    

#def PWD(): # also handles LPWD
#    return os.getcwd()

# DOWNLOAD


#def DIR (localdirectory):
#    return os.listdir(localdirectory)

# CD


# LDIR


# LCD


#**************************************************************
#Function Name: errorchecking
#Description: Checks for errors
#Parameters: None
#Return value: None
#**************************************************************
#def errorchecking()
