from subprocess import call
import sys
import glob
import filecmp
import schedule
import time
import shutil


def check(path1, path2, path3):
    comp = filecmp.cmp(path1, path2, shallow=True)
    # Comparison of files on two folders, if they aren't the same the replica folder's content is removed and then the
    # content of the source file is copied here.
    if comp is True:
        pass
        print("Content of both folder is the same!", file=open(path3, 'a'))
    else:
        files = glob.glob(path2 + "\\" + '*')
        for f in files:
            shutil.rmtree(f)
    print("Files from: " + path1 + " sent to: " + path2, file=open(path3, 'a'))
    try:
        call(["robocopy", path1, path2, "/MIR"])
        print("The content of both libraries is now the same!", file=open(path3, 'a'))
    finally:
        pass


def s(interval, path1, path2, path3):  # s stands for schedule
    schedule.every(int(interval)).minutes.do(check, path1=path1, path2=path2, path3=path3)
    while True:
        schedule.run_pending()
        time.sleep(1)


if sys.argv[1] == "-c":
    check(sys.argv[2], sys.argv[3], sys.argv[5])
    s(sys.argv[4], path1=sys.argv[2], path2=sys.argv[3], path3=sys.argv[5])
# Given are 5 arguments when calling this function via cmd: 1 -c for calling it, 2 is path/to/source, 3 path/to/replica
# 4 - time how often this app should run once again(in minutes) and 5 is the path where log file is going to be placed.
