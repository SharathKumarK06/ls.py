#!/usr/bin/env python3

import os

# pwd = os.getcwd()
pwd = "/home/sharath/"
items = []


def main():
    global pwd, items
    ls = os.listdir(pwd)

    for f in ls:
        if not os.path.exists(pwd + f):
            print(pwd + f)
            return
        if os.path.isdir(pwd + f):
            items.append(f + '/')
        else:
            items.append(f)

    items.sort()
    print("\n".join(items))


if __name__ == "__main__":
    main()
