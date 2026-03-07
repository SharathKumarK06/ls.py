#!/usr/bin/env python3

import argparse
import os

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


def list_files(pwd):
    items = []
    ls = os.listdir(pwd)

    for f in ls:
        if not os.path.exists(pwd + f):
            print(pwd + f)
            return
        if os.path.isdir(pwd + f):
            items.append(f + "/")
        else:
            items.append(f)

    items.sort()
    return items


def main():
    # pwd = os.getcwd()
    # pwd = "/home/sharath/"
    # items = list_files(pwd)
    # print("\n".join(items))
    option_parsing()
    print("Options provided:")
    print(options)


if __name__ == "__main__":
    main()
