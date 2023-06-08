#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argcount = len(sys.argv) - 1
    argsum = 0
    for i in range(argcount):
        argsum += int(sys.argv[i + 1])
    print("{}".format(argsum))
