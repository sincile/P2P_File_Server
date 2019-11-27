# Download Server

###### ***Authors:***  Christian Clark, Dylan Herbst, Brandon Kresge
###### **Creation Date:** 11/10/19
###### **Due Date:** 11/30/19
###### **Course**: CSC328-010
###### ***Filename***:  README.md
###### ***Purpose:***
Provide the user with information about the client-server program, and instructions on how to use it.

#### Description:
The file you have downloaded is a concurrent, connection-oriented, client-server program that does not require a username and password. It contains a menu of various commands you can input using the numbers listed. If you input anything else, or input without using the correct parameters, you will be given an error message and sent back to the menu.

>NOTE: THIS PROGRAM ONLY RUNS ON VERSION 3 OF PYTHON. If you are unsure about what version you are using, type "`python`" in your PuTTY window.

The following is a list of commands, what they do, and additional arguments as to avoid errors for certain commands. Input corresponding number for that command (type "1" and push the "Enter" key for the PWD command).

1. `PWD` - Outputs current server directory.

2. `DIR` - Outputs directory listing of current directory on server.

3. `CD` - Changes current server directory. After choosing command, you must input directory you wish to change to

4. `LPWD` - Outputs current directory on local client.

5. `LDIR` - Outputs directory listing of current local directory.

6. `LCD` - Changes current local directory then outputs current local directory after directory is changed.

7. `DOWNLOAD` - Allows you to download a file you want from the server. Must input a filename after selecting the command. The server will let the client know whether the file exists or not. If the file does not exist on the server the client will stop the download process. If it does the client will inform the user if the file exists locally. If the file does exist locally the client outputs that it will be overwritten if the server file is downloaded. If the file doesn't exist locally a new file is created. Then the user inputs "READY" if they wish to proceed with the download or "STOP" if they want to cancel the download.

8. `EXIT` - Sends a message to the server which lets the server know the client is disconnecting then ends the program.

#### How to compile:
 Start up PuTTY and login if necessary. Type `python3 multiport_server.py` and then `python3 client.py <IP Address> <Port Number (Optional)>`. Since Python is an interpreted language you will not need to compile any code

#### How to run:
Start up PuTTY and login if necessary. Type `python3 multiport_server.py` and then `python3 client.py <IP Address> <Port Number (Optional)>`.

#### Design overview:
The user will start up PuTTY, and login if necessary. Then the user will type `python3 multiport_server.py` and then `python3 client.py <IP Address> <Port Number (Optional)>`. After that, the user will be given a list of commands. If anything other than a command from the list is given, an error message will be displayed. Likewise, if the number of arguments is not met, an error message will also be displayed. The user can then input commands until they exit the program by pressing "8" and then "Enter".

All messages/commands follow the given algorithms/syntax provied in the originial program specifications.

#### Type of library used:
Shared because it is the default type for Python.

#### Protocol:
Syntax for messages is that user input is automatically made uppercase to correspond to commands in list. Also, port number is optional, but there is a default port number of 8000. The client and server will know when it has received all the data from the other host because of the terminating string at the end of each message which is added to the message in the library's write function before sending to the other host.


#### Known issues:
None

#### DECISIONS
- ##### Use Shared library because it is the default type for Python.

- ##### Use Python, specifically version 3

- ##### Active port ranges
Due to limitations in python's fd memory system, we had to restrict the amount of ports the server's listening on to 100. On average python can hold a little over 1000. Having 100 ports gives us plenty of leeway when dealing multiple clients and connections.
By default the active ports are 8000 - 8100

- ##### Binding issues
If there are binding issues, the server will skip these ports and print a notification on which ports are not usable. If all ports are not usable, the program will not run the server loop.

- ##### Terminating characters
We chose `*?*` as the terminating characters since this set of characters are impossible to have in files/directory names in UNIX systems. While this sequence could be possible in a file, our library only looks at the last 3 characters to determine if it's the terminating set. Although it is entirely possible to have false positive with these characters, the chances of them occuring are extremely slim

- ##### How will the client know it has received the entire directory name?
The terminating string means the entire message has been received. This is handled in the Library functions

- ##### How will the server indicate the end of the directory listing?
The server will indicate the end of the directory listing with the terminating message. This is handled in the Library functions

- ##### What will the server response be for successful and unsuccessful cd commands?
If successful, 0 . If unsuccessful, -1. This is due to both the client & server needing feedback in determining if the path/permissions to access that dir.

- ##### How does the client know when the server has completed sending the file?
The client knows because of the terminating string at the end of a message. This is handled in the Library functions

- ##### How does the server know when the client has completed sending the file?
The server knows because of the terminating string at the end of a message. This is handled in the Library functions
