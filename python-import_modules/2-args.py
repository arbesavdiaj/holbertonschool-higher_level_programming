#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argument_count = len(sys.argv)-1
if argument_count == 0:
    print("{} arguments.".format(argument_count))
elif argument_count == 1:
    print("{} argument:".format(argument_count))
    print("{}: {}".format(argument_count, sys.argv[1]))
else:
    print("{} arguments:".format(argument_count))
    for i in range(1, argument_count + 1):
        print("{}: {}".format(i, sys.argv[i]))
