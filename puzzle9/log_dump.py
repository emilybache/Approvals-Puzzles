#!/usr/bin/env python

import os
import sys
import tarfile


def main():
    print("about to gather logs", file=sys.stderr)

    log_location = os.path.join("~", "logs")

    logfile1_path = os.path.join(log_location, "app1", "errors.log")
    logfile2_path = os.path.join(log_location, "app2", "errors.log")
    logfile3_path = os.path.join(log_location, "app3", "errors.log")

    paths_to_collect = [logfile1_path, logfile2_path, logfile3_path]

    print("about to make tarfile of all logs", file=sys.stderr)
    with tarfile.open("logs.tar.gz", "w:gz") as f:
        for p in paths_to_collect:
            if os.path.exists(p):
                normalized_path = str(p).replace("\\", "/")
                print("adding file ", normalized_path, file=sys.stderr)
                f.add(p)


if __name__ == '__main__':
    main()

