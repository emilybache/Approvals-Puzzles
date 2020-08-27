#!/usr/bin/env python3
import os
import sys
import tarfile


def main():
    print("about to gather logs", sys.stderr)

    logfile1_path = os.path.join("/", "logs", "application1", "errors.log")
    logfile2_path = os.path.join("/", "logs", "application2", "errors.log")
    logfile3_path = os.path.join("logs", "local_app3", "errors.log")

    print("about to make tarfile of all logs", sys.stderr)
    with tarfile.open("logs.tar.gz", "w:gz") as f:
        f.add(logfile1_path)
        f.add(logfile2_path)
        f.add(logfile3_path)

if __name__ == '__main__':
    main()

