#!/usr/bin/python3

if __name__ == "__main__":
    """Print number of and list of argments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argments.")
    elif count == 1:
        print("1 argment:")
    else:
        print("{} argments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

