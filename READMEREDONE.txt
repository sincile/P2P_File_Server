Authors: Christian Clark, Dylan Herbst, Brandon Kresge
Creation Date: 11/10/19
Due Date: 11/30/19
Course: CSC328-010
Filename: READMEREDONE
Purpose: Provide the user with information about the client-server program, and instructions on how to use it.

Description: The file you have downloaded is a concurrent, connection-oriented, client-server program that does not require a username and password. It contains a menu of various commands you can input using the numbers listed. If you input anything else, or input without using the correct parameters, you will be given an error message and sent back to the menu.

NOTE: THIS PROGRAM ONLY RUNS ON VERSION 3 OF PYTHON. If you are unsure, type "python" in your PuTTY window.

The following is a list of commands, what they do, and additional arguments as to avoid errors for certain commands. Input corresponding number for that command (type "1" and push the "Enter" key for the PWD command).

1 PWD - Outputs current directory.

2 DIR - Outputs directory listing.

3 CD - Changes directory. After command, must input directory you wish to change to

4 LPWD - Outputs current directory on local client.

5 LDIR - Outputs local directory listing.

6 LCD - Outputs local directory. After command, must input directory you wish to change to.

7 DOWNLOAD - Allows you to download a file you want from the server. Must input a filename after. Then respond with "YES" or "NO" if you would like the file to be overwritten or not. If you wish to cancel the download, type "STOP."

8 EXIT - Stops the program.


How to run: Start up PuTTY and login if necessary. Type "python3 server.py" and then "python3 client.py".