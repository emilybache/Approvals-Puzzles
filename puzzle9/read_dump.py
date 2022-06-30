#!/usr/bin/env python

import sys
import tarfile


def main(args):
    dump_name = args[0]
    print("found dump: ", dump_name)
    with tarfile.open(dump_name, "r") as f:
        print("mode", "name", "size", "type")
        for entry in f.getmembers():
            print(entry.mode, entry.name, entry.size, entry.type)


if __name__ == "__main__":
    main(sys.argv[1:])
