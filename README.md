## Dir_Copying

Problem:
Implement a program that synchronizes two folders: source and replica. The program should maintain a full, identical copy of destination folder at replica folder.   

Requirements:   
•	Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;   
•	Synchronization should be performed periodically;   
•	File creation/copying/removal operations should be logged to a file and to the console output;   
•	Folder paths, synchronization interval and log file path should be provided using the command line arguments.   
## Install
`pip install -r requirements.txt`
## Run
`python task.py -c path/to/source/dir path/to/replica/dir time(in minutes) path/to/send/logs.log`   
The program can be run via any console, it's made for Windows as I have windows installed on my PC and I could easily check if everything goes okay during implementation.

To run program simply find it's path on your machine and then call it, by Python (or Python3) task.py(name of the file with an app) -c(it calls another parameters that are needed to run it) path\to\source\folder path\to\replica\folder 2 (time during which it's going to check if files from those folder match and if not - copy the content of source folder to replica folder again) path\to\file\where\you\want\your\logs.log

### I highly recommend opening the cmd console with admin privileges as I expect the system to block such actions.

## Quit
`alt+f4`   
This program is supposed to work for a very long time, so if you want to quit it just quit from the cmd itself.
