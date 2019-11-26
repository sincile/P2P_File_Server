# Author: Dylan Herbst
# Major: Computer Science
# Creation Date: November 15, 2019
# Due Date: November 30, 2019
# Course: CSC328
# Professor Name: Dr. Frye
# Assignment: CSproject 8: Project-Download C-S
# Filename: QOTD.py
# Purpose: This programm will connect to a server and display
# a menu of options for the user to choose from. The user may
# use the options to navigate the local directory and the server
# directory. It also has the option to download files from the
# server.
# Language: Python 3.4.10
# Execution command: python client.py <IP Address> <portNumber (Optional)>

import sys
import socket
import os
import Library

# Function name: PWD
# Description: Retrieves and outputs the server's current directory
# Parameters: sock - socket connected to server
# Return Value: None
def PWD(sock):
    Library.write("PWD", sock) #Write PWD to server
    currentDir = Library.read(sock) #Receive current server directory
    print ('Current server directory: ', currentDir, '\n') #Output server directory
    return
   
# Function name: DIR
# Description: Retrieves and outputs the directory listing from the server's current directory
# Parameters: sock - socket connected to server
# Return Value: None   
def DIR(sock):
    Library.write("DIR", sock) #Write DIR to server
    directoryListing = Library.read(sock) #Read directory listing from server
    print (directoryListing, '\n') #Output server directory listing
    return
    
# Function name: CD
# Description: Changes the server's current directory
# Parameters: sock - socket connected to server
# Return Value: None
def CD(sock):
    Library.write("CD", sock) #Write CD to server
    newDirectory = input('Please enter directory you would like to change to: ') #Prompt user for new server directory
    Library.write(newDirectory, sock) #Write user entered directory to server
    path_content = Library.read(sock) #Read 0 for success of CD or -1 for failure of CD
    if path_content == '-1':
        print('Error changing server directory.') #Output if there is a cd error
    return
    
# Function name: Disconnect
# Description: Sends a message to disconnect from the server
# Parameters: sock - socket connected to server
# Return Value: None
def Disconnect(sock):
    Library.write('BYE', sock) #Send BYE to the server
    return  

    
# Function name: LPWD
# Description: Retrieves and outputs the current local directory
# Parameters: None
# Return Value: None
def LPWD():
    try:
        currentDir = os.getcwd() #Get current local directory
    except:
        print('getcwd error') #Output if there is an error getting current local directory
        return
        
    print ('Current directory: ', currentDir, '\n') #Output current local directory
    return
    
# Function name: LDIR
# Description: Retrieves and outputs the dircectory listing of the current local directory
# Parameters: None
# Return Value: None
def LDIR():
    try:
        directoryListing = os.listdir() #Get current local directory listing
    except:
        print ('listdir error') #Output if there is an error getting current local directory listing
        
    print (directoryListing, '\n') #Print current local directory listing
    return

    
# Function name: LCD
# Description: Changes the current local directory
# Parameters: None
# Return Value: None
def LCD():
    newDirectory = input('Please enter directory you would like to change to: ') #Prompt user for new local directory to change to
    
    try:
        os.chdir(newDirectory) #Change local directory to user inputted directory
    except:
        print('chdir error') #Output if there is an error changing local directory
        
    try:
        currentDir = os.getcwd() #Get current local directory
    except:
        print('getcwd error') #Output if there is an error getting current local directory
        return
        
    print('Current directory: ', currentDir, '\n') #Output current local directory
    return
    
# Function name: Download
# Description: Prompts user for name of a file to be downloaded then downloads the file
#              if it is found on the server
# Parameters: sock - socket connected to server
# Return Value: None   
def Download(sock):
    Library.write('DOWNLOAD', sock) #Write downlaod to  the server
    fileName = input('Please enter file name: ') #Prompt user for the name of the file to be downloaded
    Library.write(fileName, sock) #Write the name of the file to be downloaded to the server`
    fileStatus = Library.read(sock) #Receive whether the file exists on the server or not
    if fileStatus == 'File Not Found':
        print('File not found.') #If the file does not exist output "File not found." and stop download process
        return
    elif fileStatus == 'READY':
        if os.path.isfile(fileName):
            print('File exists locally. If you continue with the download the file will be overwritten.') #Output if the file exists locally
        while True:
            confirmDownload = input('Type \"READY\" to continue or \"STOP\" to cancel the download: ') #Prompt for ready or stop
            confirmDownload = confirmDownload.upper()
            if confirmDownload == 'READY' or confirmDownload == 'STOP':
                break
            else:
                print('Invalid input.') #Output if user enters invalid input and prompt again.
        Library.write(confirmDownload, sock) #Write user input (ready or stop) to the server
        if confirmDownload == 'STOP':
            print('Download canceled.') #If user inputted stop then cancel the download.
            return
        fileContent = Library.read(sock) #Read contents of the file
        file = open(fileName, 'w') #Open file
        file.write(fileContent) #Write contents of server file to local file
        file.close() #Close the file
        print('File has been downloaded')
    return

# Function name: menu
# Description: Gives the user a list of commands to choose from and calls
#              the corresponding function for that command.
# Parameters: sock - socket connected to server
# Return Value: None   
def menu(sock):
     
    loop = True
    
    #Menu of commands for the user 
    while loop:
        selection = 0
    
        print ('1 - PWD')
        print ('2 - DIR')
        print ('3 - CD')
        print ('4 - LPWD')
        print ('5 - LDIR')
        print ('6 - LCD')
        print ('7 - Download')
        print ('8 - Exit')
        selection = input('Please enter the corresponding number of the option you would like to select: ')
        
        try:
            selection = int(selection) #Check if input can be converted to an integer
        except:
            selection = 9 #If input cannot be converted to an integer 9 to selection
        if selection == 1:
            PWD(sock)
        elif selection == 2:
            DIR(sock)
        elif selection == 3:
            CD(sock)
        elif selection == 4:
            LPWD()
        elif selection == 5:
            LDIR()
        elif selection == 6:
            LCD()
        elif selection == 7:
            Download(sock)
        elif selection == 8:
            Disconnect(sock)
            loop = False #Break out of menu loop when Exit command is selected
        else:
            print('Invalid selection.') #Output if invalid selection is input
        
    return

# Function name: connect
# Description: Creates a socket to connect to the server The socket is closed when finished.
# Parameters: IP - IP address of server to connect to
#             portNummber - port number to use when connecting to the server
# Return Value: None
def connect(IP, portNumber):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket
    except:
        print ('Error creating socket') #Output if socket could not be created successfully
        sys.exit(-1) #Exit if socket failed to be created
		
    server_address = (IP, int(portNumber))
    
    
    try:
        sock.connect(server_address) #Create connection to server
    except:
        print ('Error creating connection') #Output if connection to server could not be created
        sys.exit(-1) #Exit if client could not connect to server
		
    msg = Library.read(sock) #Read hello message from the server
    print (msg) #Print hello message
        
    menu(sock) #Call function to menu of commands
    
        
    try:    
        close = sock.close() #Close socket
    except:
        print ('Error closing socket') #Output if socket could not be closed successfully
        sys.exit(-1) #End program if socket fails to close successfully
        
    return

# Function name: Main
# Description: Prints IP and portNumber then calls function to connect to server.
# Parameters: sock - socket connected to server
# Return Value: None   
def main (IP, portNumber):
    print ('IP Address: ', IP)
    print ('Port number: ', portNumber)
    
    connect(IP, portNumber) #Call function to connect to server

    print('Client program ended.') #Output when program finishes
    return

if (len(sys.argv) < 2 or len(sys.argv) > 3): #Make sure format of command line arguments is correct
    print ('Usage: ', sys.argv[0], '<IP Address> <portNumber (Optional)> \n') #Print usage clause if command line arguments are input incorrectly
    sys.exit()
    
IP = sys.argv[1]
    
if (len(sys.argv) == 2):
    portNumber = 8000 #If no port number is entered the default is 8000
    
else:
    portNumber = sys.argv[2]
    
main(IP, portNumber)
