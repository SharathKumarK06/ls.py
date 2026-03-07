#!/usr/bin/env python3

import os
import sys
import argparse

prog = os.path.basename(sys.argv[0])
options = {
    # Show hidden files (files starts with ".")
    "all": False,
    # Show indicators to directory, executable, links, pipes, sockets
    # "classify": False,
    # Show diffent classes in different colors
    # "color": False,
    # File to list
    "file": False,
}


def option_parsing():
    global options
    opt_keys = options.keys()

    parser = argparse.ArgumentParser(
        usage="%(prog)s [options] [FILE]",
        description="List directory contents."
    )
    parser.add_argument(
        "-a", "--all", action="store_true",
        help="do not ignore hiddle files (entries start with '.')"
    )
    parser.add_argument(
        "file", nargs='?', default=None,
        help="list information about FILEs."
    )
    args = parser.parse_args()
    args_dict = vars(args)

    for key in opt_keys:
        options[key] = args_dict[key]

    return


def list_files(pwd):
    items = []

    try:
        items = os.listdir(pwd)
        items.sort()
    except FileNotFoundError:
        print(f"{prog}: cannot access '{pwd}': No such file or directory")
        exit(1)

    return items


def main():
    global options

    # pwd = os.getcwd()
    pwd = "~"
    option_parsing()
    items = list_files(pwd)
    print("\n".join(items))
    # print("Options provided:")
    # print(options)


if __name__ == "__main__":
    main()
