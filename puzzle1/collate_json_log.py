#!/usr/bin/env python3
import sys, json


def pretty_print_json_log(f):
    for line in f:
        fields = json.loads(line.strip())
        print(fields['msg'])


def main(args):
    if not args:
        print("no argument given: filename needed. Will exit")
        sys.exit(-1)
    inputfile = args[0]
    with open(inputfile) as f:
        pretty_print_json_log(f)


if __name__ == "__main__":
    main(sys.argv[1:])