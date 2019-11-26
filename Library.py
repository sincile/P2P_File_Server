#*******************************************************************************
#* Author: Brandon Kresge
#* Creation Date: November 19, 2019
#* Due Date: November 26th, 2019
#* Python Version: 3.7.3
#* Course: CSC328-010
#* Filename: LibraryTest.py
#* Purpose: Makes a shared library that the client and server can call functions from.
#* To run and compile: N/A; used when inputting python3 server.py and python3 client.py
#*******************************************************************************

# this file is shared, as Python libraries are shared by default

import os
import socket
terminatingstring = "*?*" # string of characters used to know if end of file, since the string should not be in a file

#**************************************************************************
#* Function Name: write
#* Description: Writes message to socket
#* Parameters: message - what is being sent to the socket, sock - a socket
#* Return value: None
#*************************************************************************

def write(message, sock):    
    message = str(message) + terminatingstring # attach terminatingstring to message
    
    message = message.encode('utf-8') # encode message
    try:
        sock.sendall(message) # send message
    except:
        print ("Sendall error")
    return

#******************************************************************************************
#Function Name: read
#Description: Reads message from socket
#Parameters: sock - a socket
#Return value: message[:-3] - the message being read, but the last three characters removed because the message has the terminating character attached
#******************************************************************************************

def read(sock):
    message = ''
    while True:
        try:
            message = message + sock.recv(256).decode('utf-8') # receive and decode message
        except:
            print ("recv error")
            break
        if (message [-3:]==terminatingstring):
            break
    return message[:-3]

#******************************************************************************************
#Function Name: validate
#Description: Validates input. If input is not from the list of commands, returns an error.
#Parameters: input - user input
#Return value: valid - input from user that is from the list of commands
#******************************************************************************************

def validate(input):
    input = input.upper()
    input = input.split(' ', 1)[0] # split command from file and directory or anything else aftter the command name
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
