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

opts_keys = [key for key, value in options.items()]


def option_parsing():
    global options, opts_keys
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
    for key in opts_keys:
        options[key] = args_dict[key]


def list_all_files(items, hidden=False):
    items_remove = []
    for index, item in enumerate(items):
        if (not hidden) and item[0].startswith("."):
            items_remove.insert(0, index)
        items[index] = item

    for i in items_remove:
        items.pop(i)
    del items_remove

    return items


def main():
    global options

    # Parse commandline options and set 'options' flags
    option_parsing()

    # TODO: Uncomment when program is ready to accept file name as cmdline args
    if options["file"]:
        pwd = options["file"]
    else:
        pwd = os.getcwd()

    if pwd.startswith("~"):
        pwd = os.path.expanduser(pwd)

    try:
        # Get list of all files and file info
        if os.path.isfile(pwd):
            items = [os.path.basename(pwd)]
        else:
            items = [
                item for item in os.listdir(pwd)
            ]

        # get files and its info
        # items = [
        #     (item, os.stat(item, follow_symlinks=False))
        #     for item in os.listdir(pwd)
        # ]

        # Sort file list
        items.sort()

        # 1. list every options provided.
        #   - check for each key, and if the value of key is true, apply the
        #   operation
        # 2. loop through `items` list and replace the items with applied
        # operations according to options given

        if options["all"]:
            items = list_all_files(items, hidden=True)
        else:
            items = list_all_files(items, hidden=False)

        print("\n".join(items))

    except FileNotFoundError:
        print(f"{prog}: cannot access '{pwd}': No such file or directory")
        exit(1)

    return


if __name__ == "__main__":
    main()
