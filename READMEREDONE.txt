Authors: Christian Clark, Dylan Herbst, Brandon Kresge
Creation Date: 11/10/19
Due Date: 11/30/19
Course: CSC328-010
Filename: READMEREDONE
Purpose: Provide the user with information about the client-server program, and instructions on how to use it.

Description: The file you have downloaded is a concurrent, connection-oriented, client-server program that does not require a username and password. It contains a menu of various commands you can input using the numbers listed. If you input anything else, or input without using the correct parameters, you will be given an error message and sent back to the menu.

NOTE: THIS PROGRAM ONLY RUNS ON VERSION 3 OF PYTHON. If you are unsure about what version you are using, type "python" in your PuTTY window.

The following is a list of commands, what they do, and additional arguments as to avoid errors for certain commands. Input corresponding number for that command (type "1" and push the "Enter" key for the PWD command).

1 PWD - Outputs current server directory.

2 DIR - Outputs directory listing of current directory on server.

3 CD - Changes current server directory. After choosing command, you must input directory you wish to change to

4 LPWD - Outputs current directory on local client.

5 LDIR - Outputs directory listing of current local directory.

6 LCD - Changes current local directory then outputs current local directory after directory is changed.

7 DOWNLOAD - Allows you to download a file you want from the server. Must input a filename after selecting the command. The server will let the client know whether the file exists or not. If the file does not exist on the server the client will stop the download process. If it does the client will inform the user if the file exists locally. If the file does exist locally the client outputs that it will be overwritten if the server file is downloaded. If the file doesn't exist locally a new file is created. Then the user inputs "READY" if they wish to proceed with the download or "STOP" if they want to cancel the download.

8 EXIT - Sends a message to the server which lets the server know the client is disconnecting then ends the program.

How to compile: Start up PuTTY and login if necessary. Type "python3 server.py" and then "python3 client.py <IP Address> <Port Number (Optional)>".

How to run: Start up PuTTY and login if necessary. Type "python3 server.py" and then "python3 client.py <IP Address> <Port Number (Optional)>".

Design overview: The user will start up PuTTY, and login if necessary. Then the user will type "python3 server.py" and then "python3 client.py <IP Address> <Port Number (Optional)>". After that, the user will be given a list of commands. If anything other than a command from the list is given, an error message will be displayed. Likewise, if the number of arguments is not met, an error message will also be displayed. The user can then input commands until they exit the program by pressing "8" and then "Enter".

Type of library used: Shared because it is the default type for Python.

Protocol: Syntax for messages is that user input is automatically made uppercase to correspond to commands in list. Also, port number is optional, but there is a default port number. The client will know when it has received all the data from the other host by ANSWER. The server will know when it has received all the data from the other host by ANSWER.

Known issues: None

DECISIONS

How will the client know it has received the entire directory name? Command separated from directory so it knows where the name of the directory begins.

How will the server indicate the end of the directory listing? 

What will the server response be for successful and unsuccessful cd commands? If successful, ANSWER. If unsuccessful, an error message will be given.

How does the client know when the server has completed sending the file? 

How does the server know when the client has completed sending the file?

