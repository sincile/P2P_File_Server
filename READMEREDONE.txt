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


How to run: Start up PuTTY and login if necessary. Type "python3 server.py" and then "python3 client.py <IP Address> <Port Number (Optional)>".
