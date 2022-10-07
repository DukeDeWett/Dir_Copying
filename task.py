from subprocess import call
import sys
import schedule
import time


def mirror(path1, path2, path3):
    try:
        call(["robocopy", path1, path2, "/MIR", "/TEE"])
        # Unfortunately it won't go to path3, so I had to print those logs to a specific file.
        print("The content of both libraries is now the same!", file=open(path3, 'a'))
    finally:
        pass


def s(interval, path1, path2, path3):  # s stands for schedule
    schedule.every(int(interval)).minutes.do(mirror, path1=path1, path2=path2, path3=path3)
    while True:
        schedule.run_pending()
        time.sleep(1)


if sys.argv[1] == "-c":
    mirror(sys.argv[2], sys.argv[3], sys.argv[5])
    s(sys.argv[4], path1=sys.argv[2], path2=sys.argv[3], path3=sys.argv[5])
# Given are 5 arguments when calling this function via cmd: 1 -c for calling it, 2 is path/to/source, 3 path/to/replica
# 4 - time how often this app should run once again(in minutes) and 5 is the path where log file is going to be placed.
